"""
Django settings for my_web_project project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-902=xml#6h%i=r1p*%-dfxu-wiz5&e3y&5(5fjk-_v8_oi3ej0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
# DEBUG = False
# ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'app_blog.apps.AppBlogConfig',
    'app_blog',   # Приложение для блога
    # 'app_users.apps.AppUsersConfig',
    # 'app_users',  # Приложение, расширяющее профили пользователей
    # 'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_web_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_web_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru-RU'

# https://stackoverflow.com/questions/29311354/how-to-set-the-timezone-in-django
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Country code(s)    TZ database name       Area(s) covered          Type       UTC offset      Time zone       Source      Notes
#                                                                               (±hh:mm)        abbreviation    file
#                                                                               STD      DST     STD   DST
# RU                 Asia/Novosibirsk       MSK+04 - Novosibirsk    Canonical  +07:00   +07:00   +07            europe
# RU                 Europe/Moscow          MSK+00 - Moscow area    Canonical  +03:00   +03:00   MSK            europe

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Novosibirsk'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# Основной url для работы со статическими файлами
STATIC_URL = 'static/'

# Основной url для управления медиафайлами
# Руководство по загрузке файлов (и изображений) в Django
# https://django.fun/ru/articles/tutorials/rukovodstvo-po-zagruzke-fajlov-i-izobrazhenij-v-django/

# MEDIA_URL = '/media/'
# # Путь хранения картинок
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# # BASE_DIR = K:\neural\pythonProject-dz26\dz26\my_web_project
# # MEDIA_ROOT = K:\neural\pythonProject-dz26\dz26\my_web_project\media

# # Путь к картинкам для профилей пользователя
# PROFILE_PICS = 'profile_pics/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
