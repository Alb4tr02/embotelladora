from .base import *
import django_on_heroku
import dj_database_url
from decouple import config


DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
SECRET_KEY= 'hlzh$&d2dt%pp2=v+2rl09khxlh(l2)tlknk=ct$oaiu@e)h8_'
django_on_heroku.settings(locals())