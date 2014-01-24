"""
Django settings for komuso project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.realpath(os.path.dirname(__file__) + '/..')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4+_55w=d2&&v$^fs7gns7(d9q#9f_wtsz-7rf!juyi1vc!v7d8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ADMINS = (
    ('Laetitia Nanni', 'laetitia.nanni@gmail.com'),
    ('Julie Po', 'pojulie07@gmail.com'),
    ('Thibault Fievet', 'thibault.fievet@gmail.com'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'komuso',
    'score-editor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.i18n",
)

ROOT_URLCONF = 'komuso.urls'

WSGI_APPLICATION = 'komuso.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.sql',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

#LANGUAGE_CODE = 'en-us'
#TIME_ZONE = 'UTC'

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr'

USE_I18N = True
USE_L10N = True

LANGUAGES = (
    ('fr', 'Francais'),
    ('en', 'Anglais'),
    ('ja', 'Japonais'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Templates
TEMPLATE_DIRS = (
    "templates"
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '{}/static'.format(BASE_DIR)
