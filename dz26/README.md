# UniversityAI-Python-Django/lesson26

<b>Engl</b>:<br>
This is a homework assignment for lesson 26" Website on Django. Django ORM" course Python developer.

<b>Russ</b>:<br>
Это домашнее задание по уроку 26 "Веб-сайт на Django. Django ORM" курса разработчик Python.


При выполнении домашнего задания решаются задачи:
- Построить модели для базы данных.
- Отразить в моделях отношения:
  - "многие ко многим" (ManyToManyField);
  - "много-к-одному" (ForeignKey).
- Используюя какие-то тестовые данные, загрузить данные в таблицы и сохранить в БД. Цель - отработать добавление в БД информации.
- Настроить админку для отображения добавленных таблиц.
- Сделать пользовательские команды. Реализованы команды:
  - fill_db: загрузка данных с БД.
  - what_time_is_it: Получение текущего времени разными способами

Для решения поставленных задач сделаны таблицы:
- Статья (Articles).
- Тэги статьи (Tags).
- Рубрики для статьи (Categories).
  
Отношения "один-к-одному" (OneToOneField) будут реализованы при работе с пользователями - при увеличении количества полей для профиля пользователя.


Папки:
- my_web_project: Файлы конфигурации проекта.
- app_blog: Приложение для блога
- my_web_project\app_blog\management: команды пользователя
- my_web_project\app_blog\init_data: исходные тестовые данные