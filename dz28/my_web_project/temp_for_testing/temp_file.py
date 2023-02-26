# import datetime
# # import os
# # from pathlib import Path
# #
# # value = 10
# # print(value % 10)
# # print(value % 100)
#
# # Как задать путь к файлу в Python?
# # https://webtort.ru/как-задать-путь-к-файлу-в-python/
#
# # print(__file__)
# # print(Path(__file__))
# # print(Path(__file__).resolve())
# # print(Path(__file__).resolve().parent)
# # print(Path(__file__).resolve().parent.parent)
# #
# # p = Path('neural/../temp_file.py')
# # print(p)
# #
# # p.resolve()
# # print(p)
# #
# # BASE_DIR = Path(__file__).resolve().parent.parent
# # MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# #
# # print(BASE_DIR)
# # print(MEDIA_ROOT)
# #
# # PROFILE_PICS = 'profile_pics'
# # print(PROFILE_PICS+'/default.png')
# import json
# import pprint
#
# import pytz
# from django.utils.timezone import make_aware
#
# from my_web_project.settings import TIME_ZONE
#
# d = datetime.date(2022, 12, 14)
# print(d)
# d = datetime.datetime(2017, 3, 5, 12, 30, 10)
# print(d)
#
# tmp_dict = {1: {'title': '''Заголовок
#                             статьи''',
#                 'body': 'Текст (тело) статьи',
#                 'created': str(datetime.date(2022, 12, 14)),
#                 'published': 'Дата опубликования статьи',
#                 'updated': (1, 3, 6, 'которой'),
#                 'author': None,
#                 'category': ['Рубрика', 1, 3, 6, 'которой', 'относится статья'],
#                 'tag': 3,
#                 'status': True,
#                 'slug': 'URL для статьи (должен быть уникальным)'
#                 }
#             }
# with open('example_json_file.txt', 'w', encoding="utf-8") as write_file:
#     json.dump(tmp_dict, write_file,
#               ensure_ascii=False, indent=4)
# # with open('example_json_file.txt', 'w', encoding="utf-8") as write_file:
# #     pprint.pprint(tmp_dict, write_file)
# with open('example_json_file.txt', 'r', encoding="utf-8") as read_file:
#     tmp_dict = json.load(read_file)
# pprint.pprint(tmp_dict)
# # преобразование ключей в целое число:
# tmp_dict = {int(k): v for k, v in tmp_dict.items()}
# pprint.pprint(tmp_dict)
# d = tmp_dict[1]['created']
# print(type(d))  # <class 'str'>
# print(d)  # 2022-12-14
# # print(d.year)    # AttributeError: 'str' object has no attribute 'year'
# dd = 'created'
# print('created: ', dd[0])
# d = datetime.datetime.strptime(d, '%Y-%m-%d').date()
# print(type(d))  # <class 'datetime.date'>
# print(d)  # 2022-12-14
# print(d.year)  # 2022
# print(d.month)  # 12
# print(d.day)  # 14
#
# # Модуль datetime
# # https://pythonworld.ru/moduli/modul-datetime.html
# # datetime.strptime(date_string, format) - преобразует строку
# # в datetime (так же, как и функция strptime из модуля time)
# # datetime.date() - объект даты (с отсечением времени)
#
# # Модуль time
# # https://pythonworld.ru/moduli/modul-time.html
#
# # Преобразование объекта DateTime из одного часового пояса в другой
# # https://translated.turbopages.org/proxy_u/en-ru.ru.3279f3a9-63b8f22d-3af86eed-74722d776562/https/www.geeksforgeeks.org/working-with-datetime-objects-and-timezones-in-python/
# # https://www.geeksforgeeks.org/working-with-datetime-objects-and-timezones-in-python/
#
# # https://stackoverflow.com/questions/3305413/how-to-preserve-timezone-when-parsing-date-time-strings-with-strptime
# tmp_dict[1]['published'] = datetime.datetime.strptime(tmp_dict[1]['created'], '%Y-%m-%d')
# tmp_dict[1]['created'] = datetime.datetime.strptime(tmp_dict[1]['created'], '%Y-%m-%d').date()
# pprint.pprint(tmp_dict)
#
# print('TIME_ZONE: ', TIME_ZONE)
# status = 'p'
# status_dict = {'p': 'p', 'Published': 'p',  # Опубликовано
#                'd': 'd', 'Draft': 'd',  # Черновик
#                'h': 'h', 'Hidden': 'h'}
# status = status_dict[status]
# print(status)
#
# # import time
#
# now = datetime.datetime.now()
# timestamp = str(now.timestamp())
# print(now)
# print(timestamp)
# # 1673025350
#
# item = "01-01-2022 00.00.00"
#
# published = (datetime.datetime.strptime(item,
#                                         '%d-%m-%Y %H.%M.%S'))
# # .replace(tzinfo=pytz.timezone(TIME_ZONE))
#
# print('published: ', published, type(published))
# published = make_aware(published, timezone=pytz.timezone("Asia/Novosibirsk"))
# print('published: ', published)
# # d = datetime.datetime.now().
# # pytz.timezone(TIME_ZONE)
# # print(d)
#
#
columns_bar = [1, 2]
weight_heights = [1, 1]
weight_heights = [[2.7, 1.4][i] for i in range(len(weight_heights))]  # + [0.7] * len(columns_bar)

print(weight_heights)


def t(d):
    s = '' if d else 'fgf'
    return {'1': s + 'ff',
            '2': s + 'ee'}


print(t(True))

print(round(5*0.5))
