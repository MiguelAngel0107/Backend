from pathlib import Path
from datetime import timedelta

import os
# Python-decouple para las variables de Braintree
from decouple import config
# Conectarse a Databases en Produccion
import dj_database_url

#from .storage_backeds import StaticStorage, MediaStorage 


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
if not DEBUG:
    ALLOWED_HOSTS = [
        'owndarkbackend.onrender.com',
        'www.owndarkbackend.onrender.com',
        'owndark.onrender.com', 
        'www.owndark.onrender.com', 
        'owndark.com',
        'www.owndark.com',
        '0.0.0.0:10000',
        '0.0.0.0'
    ]
else:
    ALLOWED_HOSTS = [
        'localhost',
        '127.0.0.1'
    ]

if not DEBUG:
    RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
    if RENDER_EXTERNAL_HOSTNAME:
        ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition
# Se tiene que hacer makemigrations, declarando cada una de las apps por individual

DJANGO_APPS = [
    # Apps for default in Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS=[
    'apps.user',
    'apps.user_profile'
]

ECOMMERCE_APPS=[
    'apps.category',
    'apps.products',
    'apps.cart',
    'apps.shipping',
    'apps.orders',
    'apps.payment',
    'apps.coupons',
]

THIRD_PARTY_APPS=[
    'storages',
    'corsheaders',
    'rest_framework',
    'djoser',
    'social_django',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'ckeditor',
    'ckeditor_uploader',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + ECOMMERCE_APPS + THIRD_PARTY_APPS

#Configuration to folder of Media
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'autoParagraph': False
    }
}

CKEDITOR_UPLOAD_PATH = "/media/"

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    'corsheaders.middleware.CorsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'build')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "es-es"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 12
}

if not DEBUG:
    CORS_ALLOWED_ORIGINS = [
        'https://owndark.onrender.com',
        'http://owndark.onrender.com',
        'https://owndark.com',
        'http://owndark.com',
        'https://owndarkbackend.onrender.com', 
        'http://0.0.0.0:10000'
    ]
else:
    CORS_ALLOWED_ORIGINS = [
        'http://localhost:3000',
        'http://localhost:8000',
        'http://127.0.0.1:8000',
        'http://127.0.0.1:3000',

    ]


if not DEBUG:
    CSRF_TRUSTED_ORIGINS = [
        'https://owndark.onrender.com',
        'http://owndark.onrender.com',
        'https://owndark.com',
        'http://owndark.com',
        'https://owndarkbackend.onrender.com',  
        'http://0.0.0.0:10000'

    ]
else:
    CSRF_TRUSTED_ORIGINS = [
        'http://localhost:3000',
        'http://localhost:8000',
        'http://127.0.0.1:8000',
        'http://127.0.0.1:3000',  
    ]


PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT', ),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10080),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESFH_TOKENS':True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    )
}

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'SET_USERNAME_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': ['http://localhost:8000/google', 'http://localhost:8000/facebook'],
    'SERIALIZERS': {
        'user_create': 'apps.user.serializers.UserCreateSerializer',
        'user': 'apps.user.serializers.UserCreateSerializer',
        'current_user': 'apps.user.serializers.UserCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
}

BT_MERCHANT_ID = config('BT_MERCHANT_ID')
BT_PUBLIC_KEY = config('BT_PUBLIC_KEY')
BT_PRIVATE_KEY = config('BT_PRIVATE_KEY')

AUTH_USER_MODEL = "user.UserAccount"

EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#-----------------------------------------------------------------------------------
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
TESTOFS3 = True
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#-----------------------------------------------------------------------------------
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


if DEBUG and TESTOFS3:

    # django-ckeditor will not work with S3 through django-storages without this line in settings.py
    AWS_QUERYSTRING_AUTH = False

    # aws settings
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = 'devinvsc'

    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_DEFAULT_ACL = 'public-read'

    # s3 static settings
    STATICFILES_LOCATION = 'static'
    STATIC_URL = '/static/'
    STATIC_ROOT = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
    STATICFILES_STORAGE = 'core.storage_backeds.StaticStorage'

    # s3 public media settings
    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'core.storage_backeds.MediaStorage'

    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'build/static'),)


if DEBUG and not TESTOFS3:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'test')
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'build/static'),)

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field


if not DEBUG:
    DEFAULT_FROM_EMAIL = 'OwnDark - Tienda de Software <admin@owndark.com>'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = config('EMAIL_HOST')
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = config('EMAIL_PORT')
    EMAIL_USE_TLS = config('EMAIL_USE_TLS')

    if TESTOFS3:
        # django-ckeditor will not work with S3 through django-storages without this line in settings.py
        AWS_QUERYSTRING_AUTH = False

        # aws settings
        AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
        AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
        AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
        AWS_DEFAULT_ACL = 'public-read'

        """# s3 static settings
        STATICFILES_LOCATION = 'static'
        STATIC_URL = '/static/'
        STATIC_ROOT = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
        STATICFILES_STORAGE = 'core.storage_backeds.StaticStorage'"""

        STATIC_URL = '/static/'
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

        # s3 public media settings
        MEDIAFILES_LOCATION = 'media'
        MEDIA_URL = '/media/'
        MEDIA_ROOT = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
        DEFAULT_FILE_STORAGE = 'core.storage_backeds.MediaStorage'

        STATICFILES_DIRS = (os.path.join(BASE_DIR, 'build/static'),)

    if not TESTOFS3:

        STATIC_URL = '/static/'
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
        STATICFILES_DIRS = (os.path.join(BASE_DIR, 'build/static'),)
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
