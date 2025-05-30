"""
WSGI config for RMF Platform Django project.

It exposes the WSGI callable as a module-level variable named ``application``.

This file is used by WSGI servers to run your project.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for 'django-admin' and WSGI
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
