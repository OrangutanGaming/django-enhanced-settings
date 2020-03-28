# django-enhanced-settings
![Tests](https://github.com/OrangutanGaming/django-enhanced-settings/workflows/Tests/badge.svg)
[![codecov](https://codecov.io/gh/OrangutanGaming/django-enhanced-settings/branch/master/graph/badge.svg)](https://codecov.io/gh/OrangutanGaming/django-enhanced-settings)
[![PyPI](https://img.shields.io/pypi/v/django-enhanced-settings)](https://pypi.org/project/django-enhanced-settings/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-enhanced-settings)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/django-enhanced-settings)

Allow for more complex and dynamic settings for Django.

## Extras
`cloud-secret-manager` - Adds support for Google Cloud Secret Manager

## Example
```py
import os

from django_enhanced_settings import Settings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings = Settings(BASE_DIR)


def __dir__():
    return settings.dir(globals())


def __getattr__(name):
    return settings.getattr(name, globals())


_DEBUG = settings.boolean_value('DJANGO_DEBUG', False)
_ALLOWED_HOSTS = settings.list_value(
    'DJANGO_ALLOWED_HOSTS',
    ['localhost'] if _DEBUG.value else [],
    split_char=';'
)
_SECRET_KEY = settings.string_value('DJANGO_SECRET_KEY', required=True)
INSTALLED_APPS = [...]
```
```py
from django.conf import setings

settings.DEBUG  # By default returns False
```
