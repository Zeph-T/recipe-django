from .base import *
import os

DEBUG = True
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', "localhost 127.0.0.1").split(' ')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
