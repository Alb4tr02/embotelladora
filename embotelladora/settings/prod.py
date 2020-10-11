from .base import *
import django_on_heroku
#import dj_database_url
#from decouple import config
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#DATABASES = {
#    'default': dj_database_url.config(
#        default=config('DATABASE_URL')
#    )
#}
SECRET_KEY= 'hlzh$&d2dt%pp2=v+2rl09khxlh(l2)tlknk=ct$oaiu@e)h8_'
django_on_heroku.settings(locals())