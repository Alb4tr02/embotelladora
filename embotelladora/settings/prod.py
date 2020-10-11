from .base import *
import django_on_heroku
import dj_database_url
#from decouple import config
import os

DEBUG = True

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}
SECRET_KEY= os.getenv('SECRET_KEY')
django_on_heroku.settings(locals())