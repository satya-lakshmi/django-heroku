"""
Django settings for djangoproject project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from dotenv import load_dotenv


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv_path = os.path.join(BASE_DIR, '.env')
import os
from dotenv import load_dotenv
load_dotenv()
SECRET = os.getenv('API_KEY')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p9+q18zx3dqn(q!gv$pj)i23(6ip_@uy*qd5(m4jr37862t6p+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'modsy',
    'chat',
    'django_slack', 
    'django.contrib.sites',

    'allauth', # new
    'allauth.account', # new
    'allauth.socialaccount', # new
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.slack',
 # new
]
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1



SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email','public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'kr_KR',
        'VERIFIED_EMAIL': True,
        'VERSION': 'v2.4'},
        
        }


ACCOUNT_AUTHENTICATION_METHOD = "email" # Defaults to username_email
ACCOUNT_USERNAME_REQUIRED = False       # Defaults to True
ACCOUNT_EMAIL_REQUIRED = True           # Defaults to False
SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_ADAPTER = "modsy.adapters.MyLoginAccountAdapter"

SOCIALACCOUNT_ADAPTER = 'modsy.adapters.MySocialAccountAdapter'
LOGIN_REDIRECT_URL = "/modsy/dashboard"



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'djangoproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoproject.wsgi.application'




# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Modsy',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '',
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/images/')

#  Add configuration for static files storage using whitenoise
CHAT_WS_SERVER_HOST = 'localhost'
CHAT_WS_SERVER_PORT = 5001
CHAT_WS_SERVER_PROTOCOL = 'ws'

if os.getcwd() == '/app':

    import dj_database_url

    db_from_env = dj_database_url.config(conn_max_age=500)

    DATABASES['default'].update(db_from_env)

    #Honor the 'X-forwarded-Proto' header for request.is_secure().

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

"""curl -X GET --header 'Accept:application/json' --header 'token:xoxb-237781680599-1126148466947-kI0FF91IR6Z6vVCuZgaPyELO' https://slack.com/api"""



