from types import MappingProxyType

VERSIONING = 'rest_framework.versioning.AcceptHeaderVersioning'

REST_FRAMEWORK_SETTINGS = MappingProxyType(
    mapping={
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        ),
        'DEFAULT_VERSIONING_CLASS': VERSIONING,
        'DEFAULT_VERSION': '1.0',
        'ALLOWED_VERSIONS': ('1.0',),
        'PAGE_SIZE': 20,
    },
)
