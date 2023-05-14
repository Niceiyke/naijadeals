"""
WSGI config for priceFinder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from priceFinder.settings_file import base

if base.DEBUG:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'priceFinder.settings_file.local')
else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'priceFinder.settings_file.production')

application = get_wsgi_application()
