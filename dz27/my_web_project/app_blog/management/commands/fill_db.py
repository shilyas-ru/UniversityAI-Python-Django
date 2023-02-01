import json
from datetime import datetime
from pathlib import Path
import pprint

import pytz
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import make_aware

from app_blog.models import Articles, Categories, Tags
from my_web_project.settings import TIME_ZONE


class Command(BaseCommand):
    # https://django.fun/ru/docs/django/4.1/howto/custom-management-commands/
    help = 'Closes the specified poll for voting'

    # BaseCommand.help
    # Краткое описание команды, которое будет напечатано в справочном сообщении,
    # когда пользователь выполнит команду python manage.py help <command>.

    def add_arguments(self, parser):
        # parser.add_argument('poll_ids', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        # Получаем строку, содержащую путь к рабочей директории:
        # dir_path = Path.cwd()
        # print(dir_path)  # Вывод: K:\neural\pythonProject-dz26\dz26\my_web_project
        # Получаем строку, содержащую путь к домашней директории:
        # dir_path = Path.home()
        # print(dir_path)  # Вывод: C:\Users\ilya
        with open(Path(Path.cwd(), 'app_blog', 'init_data', 'init_data_json_file.txt'),
                  'r',
                  encoding="utf-8") as read_file:
            tmp_dict = json.load(read_file)
            # Пример словаря в файле 'init_data_json_file.txt':
            # {
            #     "1": {
            #         "title": "Заголовок первой статьи",
            #         "body": "Текст (тело) первой статьи./nЭто новая строка в первой статье.",
            #         "created": "01-01-2022 00:00:00",
            #         "published": "02-01-2022 00:00:00",
            #         "updated":  "03-01-2022 00:00:00",
            #         "author": "Автор 1",
            #         "category": "Рубрика1",
            #         "tags": [
            #             "Тэг1",
            #             "Тэг3",
            #             "Тэг5"
            #         ],
            #         "status": "Published",
            #         "slug": "URL для первой статьи (должен быть уникальным)"
            #     }
            # }

        # pprint.pprint(tmp_dict)
        # преобразование ключей в целое число:
        # tmp_dict = {int(k): v for k, v in tmp_dict.items()}
        # pprint.pprint(tmp_dict)

        # Обрабатываем словарь.
        for item in tmp_dict.values():
            # Поля в классе Articles:
            # title, body: строка
            # created, published, updated: дата
            #     Эти поля в исходном файле записаны без указания часового пояса:
            #     "03-03-2022 00:00:00".
            #     Требуется установить часовой пояс как указано в переменной
            #     settings.TIME_ZONE;
            # author: строка
            #     отношение: ForeignKey (один-много).
            #     Проверяем, что такой автор имеется, если нет,
            #     добавляем в таблицу User.
            #     Пустым быть не может;
            # category: список
            #     отношение: ForeignKey (один-много).
            #     Проверяем, что такие категории имеются, если нет,
            #     добавляем в таблицу Categories.
            #     Тип - список.
            #     Может быть пустым;
            # tags: список
            #     отношение: ManyToManyField (много-много).
            #     Проверяем, что такой автор имеется, если нет,
            #     добавляем в таблицу Tags;
            # status: список выбора
            #     Записывается в БД  Отображается пользователю  Значение
            #     'p'                'Published'                Опубликовано
            #     'd'                'Draft'                    Черновик
            #     'h'                'Hidden'                   Скрытый
            # slug: строка
            #     Проверяем, что поле уникальное

            # Делаем проверку полей типа models.DateTimeField()
            # В БД пишется время по часовой зоне 'UTC' (часовой пояс +00:00)
            # Если переменная created принимает значение:
            # created = datetime.strptime('01-01-2022 00:00:00',
            #                             '%d-%m-%Y %H:%M:%S')
            # # Вариант 1:
            # created1 = make_aware(created,
            #                       timezone=pytz.timezone(TIME_ZONE))
            # print('created1: ', created1, type(created1))
            # # Вывод оператора print:
            # # TIME_ZONE = 'UTC'
            # # created1:  2022-01-01 00:00:00+00:00 <class 'datetime.datetime'>
            # # В базу записано значение: 2022-01-01 00:00:00
            # # TIME_ZONE = 'Asia/Novosibirsk'
            # # created1:  2022-01-01 00:00:00+07:00 <class 'datetime.datetime'>
            # # В базу записано значение: 2021-12-31 17:00:00
            #
            # # Вариант 2:
            # created2 = created.replace(tzinfo=pytz.timezone(TIME_ZONE))
            # print('created2: ', created2, type(created2))
            # # Вывод оператора print:
            # # TIME_ZONE = 'UTC'
            # # created2:  2022-01-01 00:00:00+00:00 <class 'datetime.datetime'>
            # # TIME_ZONE = 'Asia/Novosibirsk'
            # # created2:  2022-01-01 00:00:00+05:32 <class 'datetime.datetime'>

            created = ''
            try:
                created = datetime.strptime(item['created'],
                                            '%d-%m-%Y %H:%M:%S')
                created = make_aware(created, timezone=pytz.timezone(TIME_ZONE))
            except ValueError:
                print('Ошибка в дате создания - не правильный формат')

            updated = ''
            try:
                updated = datetime.strptime(item['updated'], '%d-%m-%Y %H:%M:%S')
                updated = make_aware(updated, timezone=pytz.timezone(TIME_ZONE))
            except ValueError:
                print('Ошибка в дате обновления - не правильный формат')

            published = ''
            # Значение может отсутствовать, то есть, на вхоже будет None
            try:
                published = (make_aware(datetime.strptime(item['published'],
                                                          '%d-%m-%Y %H:%M:%S'),
                                        timezone=pytz.timezone(TIME_ZONE))
                             if item['published'] is not None
                             else None)
            except ValueError:
                print('Ошибка в дате опубликования - не правильный формат')

            # Проверяем корректность данных для статуса статьи
            status = item['status']
            if status in ['p', 'Published',  # Опубликовано
                          'd', 'Draft',  # Черновик
                          'h', 'Hidden']:  # Скрытый
                status = status[0].lower()
                # вариант на случай, если ключ и отображаемое значение
                # никак не будут алгоритмично преобразовываться.
                # Ключи - то, что в исходном файле, значения - то,
                # что надо получить в итоге:
                #     status_dict = {'p': 'p', 'Published': 'p',  # Опубликовано
                #                    'd': 'd', 'Draft': 'd',      # Черновик
                #                    'h': 'h', 'Hidden': 'h'}     # Скрытый
                #     status = status_dict[status]
            else:
                print('Ошибка в статусе статьи - не правильное значение.' +
                      ' Устанавливаем тип: Черновик (Draft)')
                status = 'd'

            # Проверяем уникальность поля slug.
            slug = item['slug']
            slug_is_present = Articles.objects.filter(slug=slug).exists()
            if slug_is_present:
                print("Ошибка в поле slug - такой адрес уже имеется.")
                # В идеале тут генерировать случайную довеску к адресу
                # Пока запрашивается текущая дата и время
                # и преобразовывается в юникс-формат:
                # datetime.now():                2023-01-07 00:21:32.722980
                # datetime.now().timestamp():    1673025692.72298
                slug = item['slug'] + str(datetime.now().timestamp())

            # Примеры использования API отношений между моделями
            # https://django.fun/ru/docs/django/4.1/topics/db/examples/
            #  - Отношения многие ко многим:
            #    https://django.fun/ru/docs/django/4.1/topics/db/examples/many_to_many/
            #  - Отношения много-к-одному:
            #    https://django.fun/ru/docs/django/4.1/topics/db/examples/many_to_one/
            #  - Отношения один-к-одному:
            #    https://django.fun/ru/docs/django/4.1/topics/db/examples/one_to_one/

            # - Создание запросов
            #   https://django.fun/ru/docs/django/4.1/topics/db/queries/
            # - Сохранение полей ForeignKey и ManyToManyField
            #   https://django.fun/ru/docs/django/4.1/topics/db/queries/#saving-foreignkey-and-manytomanyfield-fields

            # Определяем автора в таблице пользователей.
            try:
                author = User.objects.get(username=item['author'])
            except ObjectDoesNotExist:
                # Создание пользователей:
                # https://django.fun/ru/docs/django/4.1/topics/auth/default/#creating-users
                # class models.UserManager метод create_user:
                # https://django.fun/ru/docs/django/4.1/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user

                # О программном создании пользователей написано в статье:
                # Как создавать пользовательские команды управления Django
                # https://tretyakov.net/post/kak-sozdavat-polzovatelskie-komandy-upravleniya-django/
                author = User.objects.create_user(item['author'],
                                                  email='',
                                                  password='TempPassword')

            # Можно сразу при создании записи присваивать значение.
            # Определяем категорию в таблице категорий.
            category = None
            if item['category']:
                try:
                    category = Categories.objects.get_or_create(name=item['category'])[0]
                except MultipleObjectsReturned:
                    # Присутствует более одной категории - это ошибка в БД.
                    # Берём самое первое значение и его используем.
                    print('Присутствует более одной категории для значения:', item['category'])
                    category = Categories.objects.filter(name=item['category']).first()

            # https://metanit.com/python/django/5.12.php
            # Метод get_or_create() (и его асинхронная версия aget_or_create)
            # возвращает объект, а если его нет в бд, то добавляет в бд новый объект.
            # Метод возвращает кортеж из двух элементов:
            # (object, created)
            # - object: сам объект (найденный или добавленный)
            # - created: булевое значение, которое хранит True, если добавление
            #            прошло успешно и False, если объект был в БД.
            # Если в таблице уже есть несколько объектов (два и больше) с
            # указанными значениями, то сгенерируется исключение MultipleObjectsReturned

            # Создаём запись в таблице Articles
            article = Articles.objects.create(title=item['title'],
                                              body=item['body'],
                                              created=created,
                                              published=published,
                                              updated=updated,
                                              status=status,
                                              author=author,
                                              category=category,
                                              slug=slug)

            # Определяем категорию в таблице категорий.
            # этот вариант можно использовать, если тре требуется
            # изменить ссылку на категорию для уже созданной статьи.
            # if item['category']:
            #     category = Categories.objects.get_or_create(name=item['category'])[0]
            #     article.category = category
            #     article.save()

            # Определяем тэги в таблице тэгов и добавляем к статье.
            if item['tags']:
                # Условие if item['tags'] требуется, если в исходном файле отсутствие
                # тэгов будет кодироваться значением null, а не пустым списком [].
                # Если отсутствие тэгов кодируется только пустым списком - то условие
                # можно убрать.
                for tag_name in item['tags']:
                    try:
                        tag = Tags.objects.get_or_create(name=tag_name)[0]
                    except MultipleObjectsReturned:
                        # Присутствует более одного тэга - это ошибка в БД.
                        # Берём самое первое значение и его используем.
                        print('Присутствует более одного тэга для значения:', tag_name)
                        tag = Tags.objects.filter(name=tag_name).first()
                    article.tag.add(tag)
