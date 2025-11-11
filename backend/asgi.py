"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Get the ASGI application
application = get_asgi_application()

# Note: Gunicorn / Uvicorn workers handle signals. Avoid custom signal
# handlers here so we don't interfere with the server's graceful shutdown.
