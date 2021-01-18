from typing import Tuple

from .default_apps import DEFAULT_APPS
from .default_middleware import DEFAULT_MIDDLEWARE
from .rest_framework_settings import REST_FRAMEWORK_SETTINGS
from .validators import DEFAULT_VALIDATORS
from .templates import DEFAULT_TEMPLATES

__all__: Tuple = (
    'DEFAULT_APPS', 'DEFAULT_MIDDLEWARE', 'REST_FRAMEWORK_SETTINGS',
    'DEFAULT_VALIDATORS', 'DEFAULT_TEMPLATES'
)
