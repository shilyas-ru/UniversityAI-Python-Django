from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from app_blog.models import Articles

from .forms import ContactForm

# Create your views here.


def main_view(request):
    # выбираем первые 3 объекта, что на уровне базы
    # данных транслируется в SQL-выражение LIMIT 3
    articles = Articles.objects.all()[:3]
    return render(request, 'app_blog/index.html', context={'articles': articles})
    # return render(request, 'app_blog/index.html')


def about_view(request):
    # posts = Post.objects.all()
    # return render(request, 'app_blog/index.html', context={'posts': posts})
    return render(request, 'app_blog/about.html')


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
