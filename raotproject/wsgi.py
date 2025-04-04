"""
WSGI config for raotproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Make sure it's using the main settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'raotproject.settings')

application = get_wsgi_application()
