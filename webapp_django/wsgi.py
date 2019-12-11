"""
WSGI config for webapp_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp_django.settings')

application = get_wsgi_application()
