from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zero_db',
        'USER': 'admin',
        'PASSWORD': 'gacon132456',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}
