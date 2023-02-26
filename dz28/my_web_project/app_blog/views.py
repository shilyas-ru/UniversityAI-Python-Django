from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from app_blog.models import Articles, Categories

from .forms import ContactForm

# Create your views here.


def main_view(request):
    # выбираем первые 3 объекта, что на уровне базы
    # данных транслируется в SQL-выражение LIMIT 3
    articles = Articles.objects.all()[:3]
    return render(request, 'app_blog/index.html', context={'articles': articles})
    # return render(request, 'app_blog/index.html')


def about_view(request):
    return render(request,
                  'app_blog/about.html',
                  context={'img_file_name': 'home-bg.jpg'})
    # posts = Post.objects.all()
    # return render(request, 'app_blog/about.html')


def contact_view(request):
    # posts = Post.objects.all()
    # return render(request, 'app_blog/index.html', context={'posts': posts})
    if request.method == 'POST':
        # Обрабатываем заполненную форму
        form = ContactForm(request.POST)
        if form.is_valid():
            # Получить данные из форы
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            send_mail(
                'Contact message',
                f'Ваш сообщение {message} принято',
                'from@example.com',
                [email],
                fail_silently=True,
            )
            # return HttpResponseRedirect(reverse('blog:index',
            #                                     kwargs={'send_email': 'Сообщение отправлено'}))
            return HttpResponseRedirect(reverse('blog:index'))
    else:
        # Отрисовка пустой формы
        form = ContactForm()
        return render(request, 'app_blog/contact.html', context={'form': form})
    # author = articles.author.first_name


def post_view(request, id):
    articles = get_object_or_404(Articles, id=id)
    author = articles.author

    print('author:', author)
    print('type(author):', type(author))
    print('author.username:', author.username)
    print('author.id:', author.id)

    return render(request, 'app_blog/post.html', context={'articles': articles,
                                                          'author': author})
    # return render(request, 'app_blog/post.html')


def main_empty_view(request):
    # posts = Post.objects.all()
    # return render(request, 'app_blog/index.html', context={'posts': posts})
    return render(request, 'app_blog/empty/index.html')


def about_empty_view(request):
    # posts = Post.objects.all()
    # return render(request, 'app_blog/index.html', context={'posts': posts})
    return render(request, 'app_blog/empty/about.html')


def contact_empty_view(request):
    # posts = Post.objects.all()
    # return render(request, 'app_blog/index.html', context={'posts': posts})
    return render(request, 'app_blog/empty/contact.html')


def post_empty_view(request):
    # posts = Post.objects.all()
    # return render(request, 'app_blog/index.html', context={'posts': posts})
    return render(request, 'app_blog/empty/post.html')


# список категорий
class Categories_ListView(ListView):
    model = Categories
    template_name = 'app_blog/categories_list.html'
    context_object_name = 'categories'

    def get_context_data(self, *args, **kwargs):
        # Отвечает за передачу параметров в контекст
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'Список категорий (контекст - переменная name)'
        return context


# Одна категория
class Categories_DetailView(DetailView):
    model = Categories
    template_name = 'app_blog/category.html'
    context_object_name = 'category'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category_id = None
        self.category_name = None

    def get_context_data(self, *args, **kwargs):
        # Отвечает за передачу параметров в контекст
        context = super().get_context_data(*args, **kwargs)
        context['name'] = f'Категория: {self.category_name}'
        return context

    def get(self, request, *args, **kwargs):
        # Метод обработки get запроса
        self.category_id = kwargs['pk']
        is_present = Categories.objects.filter(pk=self.category_id).exists()
        if is_present:
            self.category_name = Categories.objects.get(pk=self.category_id).name
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        # Получение этого объекта
        return get_object_or_404(Categories, pk=self.category_id)


# создание категории
class Categories_CreateView(CreateView):
    # form_class =
    fields = '__all__'
    model = Categories
    success_url = reverse_lazy('my_blog_app:cat_list')
    template_name = 'app_blog/category_create.html'

    def post(self, request, *args, **kwargs):
        # Пришел пост запрос

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Метод срабатывает после того как форма валидна
        return super().form_valid(form)


class Categories_UpdataView(UpdateView):
    fields = '__all__'
    model = Categories
    success_url = reverse_lazy('my_blog_app:cat_list')
    template_name = 'app_blog/category_create.html'


class Categories_DeleteView(DeleteView):
    model = Categories
    success_url = reverse_lazy('my_blog_app:cat_list')
    template_name = 'app_blog/category_delete_confirm.html'  # Шаблон для подтверждения удаления. Похож на шаблон детализации
