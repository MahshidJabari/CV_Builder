import json
import logging
from datetime import timedelta
from cv.base_settings import *

from environs import Env

SETTINGS += 'main'
env = Env()

env.read_env(recurse=False, path=join('.env'))  # noqa

SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG")
VERSION = env("VERSION")
DJANGO_ENV = env("DJANGO_ENV")

ACCESS_TOKEN_LIFETIME = env.int('ACCESS_TOKEN_LIFETIME_HOURS')

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=ACCESS_TOKEN_LIFETIME),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

with env.prefixed('CORS_ORIGIN_') as e:
    CORS_ORIGIN_ALLOW_ALL = e.bool('ALLOW_ALL')
    CORS_ORIGIN_WHITELIST = e.list('WHITELIST', ['http://*'])

with env.prefixed('DB_') as e:
    DATABASES = {
        'default': dict(
            ENGINE='django.db.backends.postgresql_psycopg2',
            NAME=e('NAME'),
            USER=e('USER'),
            PASSWORD=e('PASS'),
            HOST=e('HOST'),
            PORT=e('PORT')
        )
    }

with env.prefixed('EMAIL_') as e:
    EMAIL_ENABLED = e.bool('ENABLED')
    if EMAIL_ENABLED:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = e('HOST')
        EMAIL_USE_TLS = e.bool('USE_TLS')
        EMAIL_PORT = e.int('PORT')
        EMAIL_HOST_USER = e('HOST_USER')
        EMAIL_HOST_PASSWORD = e('HOST_PASSWORD')
        EMAIL_USE_SSl = e.bool('USE_SSL')
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
