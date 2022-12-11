"""
Django settings for domain project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys
from puput import PUPUT_APPS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

DEBUG = 'DEBUG' in os.environ and (os.environ['DEBUG'] == '1' or os.environ['DEBUG'] == "True")
print("Debug Mode: %s" % DEBUG)

# Security Key on prod is a secret. if you need to debug, uncomment the line below
if 'SECRET_KEY' not in os.environ:
    if not DEBUG:
        raise KeyError("No Secret Key Provided for a non-Debug Server!")
    os.environ['SECRET_KEY'] = 'This1s4$tr0ngD38ugK3y'  # Close Enough :)

SECRET_KEY = os.environ['SECRET_KEY']
DB_PASS = os.environ['DB_PASS'] if 'DB_PASS' in os.environ else ""

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'personal_site',
) + PUPUT_APPS + ('wagtailtinymce',)

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.core.middleware.SiteMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'domain.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # os.path.join(BASE_DIR, 'personal_site/templates')
            os.path.join(BASE_DIR, "templates"),  # This is used to override templates from any installed app (e.g. Puput)
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

WSGI_APPLICATION = 'domain.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

MYSQL = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'personal_site',
        'USER': 'personal_site',
        'PASSWORD': DB_PASS,
        'HOST': 'localhost',
        'PORT': '',
    }

SQLITE = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # Consider changing this into an OS env var
    }

DATABASES = {
    'default': MYSQL if DB_PASS != "" else SQLITE
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

WAGTAIL_SITE_NAME = 'Javier E. Fajardo\'s Blog'

WAGTAILADMIN_RICH_TEXT_EDITORS = {
   'default': {
       'WIDGET': 'domain.tiny_mce_wrapper.TinyMCEWrapper'
   },
}

from wagtail.embeds.oembed_providers import youtube, vimeo
WAGTAILEMBEDS_FINDERS = [
    {
        'class': 'domain.youtube_oembed.YoutubeOEmbedFinder',
        'providers': [
            {
                "endpoint": "https://www.youtube.com/oembed",
                "urls": [
                    r'^https?://(?:[-\w]+\.)?youtube\.com/watch.+$',
                    r'^https?://(?:[-\w]+\.)?youtube\.com/v/.+$',
                    r'^https?://youtu\.be/.+$',
                    r'^https?://(?:[-\w]+\.)?youtube\.com/user/.+$',
                    r'^https?://(?:[-\w]+\.)?youtube\.com/[^#?/]+#[^#?/]+/.+$',
                    r'^https?://m\.youtube\.com/index.+$',
                    r'^https?://(?:[-\w]+\.)?youtube\.com/profile.+$',
                    r'^https?://(?:[-\w]+\.)?youtube\.com/view_play_list.+$',
                    r'^https?://(?:[-\w]+\.)?youtube\.com/playlist.+$',
                ],
            }
        ],
        'options': {'scheme': 'https'}
    },
    {
        'class': 'wagtail.embeds.finders.oembed',
    }
]