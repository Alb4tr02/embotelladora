from .base import *
import django_on_heroku
import dj_database_url
from decouple import config


DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
django_on_heroku.settings(locals())