"""
Django settings for kbbs project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import codecs
import socket
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^ucnnzkve7%5wp_q6$hrnf-s!##1x5ih+l3#56__8&#plqaot5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = socket.gethostname() == 'Yohans-MacBook-Air.local'

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'import_export',
    'partes',
    'responsables_dhl',
    'envios_kbbs',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kbbs.urls'

WSGI_APPLICATION = 'kbbs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if DEBUG:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kbbs',
        'USER': 'yohan',
        'PASSWORD': os.environ['pass_db'],
        'HOST': 'localhost',
        'PORT':'5432',
        }
    }
else:
    import dj_database_url
    DATABASES = { 'default' : dj_database_url.config()}
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


    # Static asset configuration
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # STATIC_ROOT = 'staticfiles'
    # STATIC_URL = '/static/'

    # STATICFILES_DIRS = (
    #     os.path.join(BASE_DIR, 'static'),
    # )

STATIC_URL = '/static/'



AWS_STORAGE_BUCKET_NAME = 'kbbs'
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'



