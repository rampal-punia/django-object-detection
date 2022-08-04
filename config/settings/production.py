"""
Django settings for {{ project_name }} project in production mode

This fill will be automatically used when using a dedicated application server.
See `base.py` for basic settings.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""


from .base import *


DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ""

# remember to set this to your expected hostnames
ALLOWED_HOSTS = []
