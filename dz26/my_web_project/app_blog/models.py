from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=50,
                            help_text='Наименование категории')
    slug = models.SlugField(max_length=250,
                            null=True,
                            blank=True,
                            unique=True,
                            help_text='URL для указанной категории (должен быть уникальным)')

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=50,
                            help_text='Наименование тэга')
    slug = models.SlugField(max_length=250,
                            null=True,
                            blank=True,
                            unique=True,
                            help_text='URL для указанного тэга (должен быть уникальным)')

    def __str__(self):
        return self.name


class Articles(models.Model):
    # Записывается в БД
    PUBLISHED_STATUS = 'p'  # Опубликовано
    DRAFT_STATUS = 'd'  # Черновик
    HIDDEN_STATUS = 'h'  # Скрытый (вариант: Withdrawn - Изъятый
    # Отображается пользователю
    PUBLISHED_VALUE = 'Published'  # Опубликовано
    DRAFT_VALUE = 'Draft'  # Черновик
    HIDDEN_VALUE = 'Hidden'  # Скрытый (вариант: Withdrawn - Изъятый)
    STATUS_CHOICES = [
        (PUBLISHED_STATUS, PUBLISHED_VALUE),
        (DRAFT_STATUS, DRAFT_VALUE),
        (HIDDEN_STATUS, HIDDEN_VALUE),
    ]

    title = models.CharField(max_length=100,
                             help_text='Заголовок статьи')
    body = models.TextField(help_text='Текст (тело) статьи')
    # https://django.fun/ru/docs/django/4.1/ref/models/fields/#datefield
    #  DateField.auto_now¶
    #
    # DateField.auto_now_add
    # Автоматически установить поле на сейчас, когда объект создается впервые.
    # Полезно для создания меток времени. Обратите внимание, что текущая дата
    # всегда используется; это не просто значение по умолчанию, которое вы
    # можете переопределить. Так что даже если вы установите значение для
    # этого поля при создании объекта, оно будет проигнорировано. Если вы
    # хотите изменить это поле, установите вместо auto_now_add=True следующее:
    #     Для DateField: default=date.today - от datetime.date.today()
    #     Для DateTimeField: default=timezone.now - от django.utils.timezone.now()

    # created = models.DateTimeField(auto_now_add=True,
    created = models.DateTimeField(default=timezone.now,
                                   help_text='Дата создания статьи')

    published = models.DateTimeField(null=True,
                                     blank=True,
                                     default=None,
                                     help_text='Дата опубликования статьи')

    # https://django.fun/ru/docs/django/4.1/ref/models/fields/#datefield
    #  DateField.auto_now
    #
    #     Автоматически устанавливать текущую дату каждый раз, когда объект
    #     сохраняется. Полезно для отметок времени последнего изменения.
    #     Обратите внимание, что текущая дата всегда используется; это не
    #     просто значение по умолчанию, которое вы можете переопределить.
    # updated = models.DateTimeField(auto_now=True,
    updated = models.DateTimeField(default=timezone.now,
                                   help_text='Дата обновления (изменения) статьи')
    author = models.ForeignKey(User,
                               default=None,
                               on_delete=models.CASCADE,
                               help_text='Автор статьи')
    category = models.ForeignKey(Categories,
                                 blank=True,
                                 null=True,
                                 default=None,
                                 on_delete=models.CASCADE,
                                 help_text='Рубрика, к которой относится статья')
    tag = models.ManyToManyField(Tags,
                                 help_text='Тэги, связанные со статьёй')
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICES,
                              default=DRAFT_STATUS,
                              help_text='Статус статьи (Published/опубликовано, Draft/черновик, Hidden/скрыто)')
    slug = models.SlugField(max_length=250,
                            null=True,
                            blank=True,
                            unique=True,
                            help_text='URL для статьи (должен быть уникальным)')

    def __str__(self):
        return self.title


class Toc(models.Model):
    name = models.CharField(max_length=100,
                            help_text='Наименование пункта оглавления')
    path = models.CharField(max_length=100,
                            help_text='Составной путь для каждого из пунк-тов оглавления.')
    menu_order = models.IntegerField(help_text='Указывается порядок в пределах своего уровня')
    article = models.ForeignKey(Articles,
                                null=True,
                                blank=True,
                                default=None,
                                on_delete=models.SET_NULL,
                                help_text='Ссылка на статью')
    slug = models.SlugField(max_length=250,
                            null=True,
                            blank=True,
                            unique=True,
                            help_text='URL для пункта оглавления (должен быть уникальным)')

    def __str__(self):
        return self.name
