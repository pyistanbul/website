# coding: utf-8

import os

from django.core.urlresolvers import reverse_lazy

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
    'djangospam.cookie.middleware.SpamCookieMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'blog.context_processors.export_blog_settings',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)

ROOT_URLCONF = 'pyist.urls'


WSGI_APPLICATION = 'pyist.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
)

THIRD_PARTY_APPS = (
    'django_gravatar',
    'markitup',
    'nose',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
)

LOCAL_APPS = (
    'jobs',
    'people',
    'presentations',
    'blog',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
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

# Blog Settings

BLOG = {
    'TITLE': 'Python İstanbul',
    'DESCRIPTION': 'Python İstanbul Günlüğü',
    'LIMIT': 5,
    'URL': 'http://pyistanbul.org/',
    'DISQUS_USERNAME': 'pyistanbul',
    'USE_DISQUS': False,
}

# Djangospam Settings
DJANGOSPAM_COOKIE_KEY = 'argumentclinic'
DJANGOSPAM_LOG = 'spam.log'

# Nose Settings
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# auth
LOGIN_REDIRECT_URL = reverse_lazy('blog:home')

# allauth settings
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_LOGOUT_REDIRECT_URL = reverse_lazy('account_login')
