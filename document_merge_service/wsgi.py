"""
WSGI config for project_app2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

import django
from django.core.wsgi import get_wsgi_application
from django.urls import get_resolver


def setup_environment():
    """Execute setup for WSGI applications."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "document_merge_service.settings")
    django.setup(set_prefix=False)

    # Load URLconf before gunicorn forks off, allowing to
    # share more memory between the workers
    _ = get_resolver().url_patterns


setup_environment()


application = get_wsgi_application()
