"""
Django settings for protoBase project.
Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!e2mfht*_mo5gfjbc$jm=rtke4ku)bq$+3x7dn346=ed@diba&'

ALLOWED_HOSTS = ['*']

LOGIN_REDIRECT_URL = '/'


# Application definition

AUTH_USER_MODEL = 'auth.User'
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jsonfield2', 
    'reversion',
    'protoLib', 
    'protoExt', 
    'prototype', 
    'rai01ref', 

    # 'import_export',     : deprecate warning importlib 
    'taggit',

    # 'rai00base', 
    # 'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'reversion.middleware.RevisionMiddleware',
    'protoLib.middleware.CurrentUserMiddleware',
)

ROOT_URLCONF = 'protoBase.urls'

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

WSGI_APPLICATION = 'protoBase.wsgi.application'



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = 'America/Montreal'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")


# ======================   DEPLOY 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
LOG_FILE = os.path.join(BASE_DIR, 'errors.log')

# DATABASES = {}
# Db HEROKU 
# try:
#     import dj_database_url
#     DATABASES['default'] =  dj_database_url.config()
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# except ImportError:
#     pass

# SoftMach Settings ==========================================

PROTO_PREFIX = "prototype.ProtoTable."
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


try:
    from .local_settings import *  # @UnusedWildImport
except ImportError:
    pass

