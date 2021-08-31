from dashboardpy.settings.base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dashboardDB',
        'USER': 'dashboardUser',
        'PASSWORD': 'dashboardPwd',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

STATIC_ROOT = '/home/dashboard/static'
MEDIA_ROOT = '/home/dashboard/media'
