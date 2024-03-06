from .base import *  # noqa
from .base import env

CORS_ALLOW_ALL_ORIGINS = True

SECRET_KEY = env('DJANGO_SECRET_KEY', default='BbQeXUvDo-2CxB1jszikeNTQG69VakG5naqdpD2_UyEDPRGSdbQ',)

DEBUG = env.bool("DJANGO_DEBUG", False)

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['http://localhost:8080']
