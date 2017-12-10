from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

USE_L10N = False
DATE_FORMAT = 'd/m/Y'
DATETIME_FORMAT = 'd/m/Y H:i:s'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'hungnv132.net']

CKEDITOR_UPLOAD_PATH = 'static/images/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'require',
    'ckeditor',
    'ckeditor_uploader',
    'stock',
    'blog'
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zero_db',
        'USER': 'admin',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)
COMPRESS_ENABLED = True

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

# settings CKEditor

CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_RESTRICT_BY_DATE = False
CKEDITOR_UPLOAD_PATH = 'blog/'
CKEDITOR_FILENAME_GENERATOR = 'core.utils.get_image_filename'
CKEDITOR_CONFIGS = {
    'default': {
        'height': 300,
        'width': 1200,
    },
}