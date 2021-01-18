# TODO: always check for "python manage.py check --deploy"
from os.path import dirname, abspath, join
from types import MappingProxyType
from typing import Tuple

import sentry_sdk
from corsheaders.defaults import default_methods, default_headers
from environ import Env
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration

from .helpers import (
    DEFAULT_APPS, DEFAULT_MIDDLEWARE, REST_FRAMEWORK_SETTINGS,
    DEFAULT_VALIDATORS, DEFAULT_TEMPLATES
)

BASE_DIR: str = dirname(dirname(abspath(__file__)))
# Environment variables
env: Env = Env()
Env.read_env()
# Sentry
SENTRY_DSN: str = env.str(var='SENTRY_DSN')
sentry_sdk.init(
    dsn=SENTRY_DSN, integrations=(DjangoIntegration(), CeleryIntegration())
)
# Django
DEBUG: bool = env.bool(var='DEBUG')
SECRET_KEY: str = env.str(var='SECRET_KEY')
APPEND_SLASH: bool = True
ALLOWED_HOSTS: Tuple = ('*',)
INSTALLED_APPS: Tuple = DEFAULT_APPS
MIDDLEWARE: Tuple = DEFAULT_MIDDLEWARE
ROOT_URLCONF: str = 'core.urls'
TEMPLATES: Tuple = DEFAULT_TEMPLATES
WSGI_APPLICATION: str = 'core.wsgi.application'
DATABASES: MappingProxyType = MappingProxyType({'default': env.db()})
AUTH_PASSWORD_VALIDATORS: Tuple = DEFAULT_VALIDATORS
# ASGI
ASGI_APPLICATION: str = 'core.asgi.application'
# Security
SECURE_BROWSER_XSS_FILTER: bool = True
SESSION_COOKIE_SECURE: bool = False
X_FRAME_OPTIONS: str = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF: bool = True
CSRF_COOKIE_SECURE: bool = False
TIME_ZONE: str = env.str(var='TIME_ZONE')
USE_TZ: bool = True
STATIC_URL: str = '/static/'
STATIC_ROOT: str = join(BASE_DIR, 'staticfiles')
MEDIA_URL: str = '/media/'
MEDIA_ROOT: str = join(BASE_DIR, 'media')
# CorsHeaders
CORS_ORIGIN_ALLOW_ALL: bool = True
CORS_ALLOW_METHODS: Tuple = default_methods
CORS_ALLOW_HEADERS: Tuple = default_headers
CORS_ALLOW_CREDENTIALS: bool = True
# Rest framework
REST_FRAMEWORK: MappingProxyType = REST_FRAMEWORK_SETTINGS
# Celery
CELERY_BROKER_URL: str = env.str(var='CELERY_BROKER_URL')
CELERY_RESULT_BACKEND: str = env.str(var='CELERY_RESULT_BACKEND')
CELERY_TIMEZONE: str = env.str(var='CELERY_TIMEZONE')
CELERY_ENABLE_UTC: bool = True
CELERY_ACCEPT_CONTENT: Tuple = ('application/json',)
CELERY_TASK_SERIALIZER: str = 'json'
CELERY_RESULT_SERIALIZER: str = 'json'
CELERY_TASK_ACKS_LATE: bool = True
