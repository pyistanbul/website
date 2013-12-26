# coding=utf-8
import os

PROJECT_PATH = os.path.abspath(os.getcwd())

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Fatih Erikli', 'fatiherikli@gmail.com'),
    ('Berker Peksag', 'berkerpeksag@gmail.com'),
)

MANAGERS = ADMINS
ALLOWED_HOSTS = [
    '127.0.0.1',
]
TIME_ZONE = 'Europe/Istanbul'
LANGUAGE_CODE = 'TR-tr'
SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = '{:s}/static/'.format(PROJECT_PATH)
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    '{:s}/static_files/'.format(PROJECT_PATH),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '#1f*6@=e@*7t1yk_!gef=jn!pc5#mv_%)=8__y8*gi0&0t7=u('

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'pyist.urls'


WSGI_APPLICATION = 'pyist.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'south',
    'gravatar',
    'markitup',
    'radpress',
    'nose',

    'jobs',
    'people',
    'presentations',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Database Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '{:s}/data/db.sqlite'.format(PROJECT_PATH),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Markitup Settings
MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': False})

# Radpress Settings
RADPRESS_TITLE = 'Python İstanbul'
RADPRESS_DESCRIPTION = "Python İstanbul Günlüğü"
RADPRESS_LIMIT = 5
RADPRESS_DISQUS = 'pyistanbul'

# Nose Settings
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Djangospam Settings
AKISMET_BLOG = 'http://pyistanbul.org'
AKISMET_KEY = ''
AKISMET_USERAGENT = 'pyistanbul'
AKISMET_USERAGENT_VERSION = '0.1'
DISCARD_SPAM = True
