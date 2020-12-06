from .base import *
import django_on_heroku
import dj_database_url
#from decouple import config
import os

DEBUG = True
ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

DATABASES = {
    'default': dj_database_url.config(default=os.environ['DATABASE_URL'])
}

SECRET_KEY = os.getenv('SECRET_KEY')
django_on_heroku.settings(locals())