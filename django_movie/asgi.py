"""
ASGI config for django_movie project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_movie.settings')

application = get_asgi_application()

# Need for synhronized web servers
# wsgi and asgi are connected
