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

# Django's get_asgi_application() returns a bare ASGI app.
# It supports the 'http' and 'websocket' scopes but may not fully support 'lifespan'.
# Wrapping with a simple lifespan handler ensures Uvicorn doesn't warn about missing support.
# This is especially important for Render deployments using UvicornWorker.

class LifespanWrapper:
    """Wrap Django ASGI app to handle lifespan protocol gracefully."""
    
    def __init__(self, asgi_app):
        self.asgi_app = asgi_app
    
    async def __call__(self, scope, receive, send):
        if scope['type'] == 'lifespan':
            # Lifespan events: startup, shutdown. Just ack them without doing anything special.
            # Django's app doesn't need explicit lifespan setup in most cases.
            while True:
                message = await receive()
                if message['type'] == 'lifespan.startup':
                    await send({'type': 'lifespan.startup.complete'})
                elif message['type'] == 'lifespan.shutdown':
                    await send({'type': 'lifespan.shutdown.complete'})
                    return
        else:
            # Delegate HTTP/WebSocket to Django's ASGI app
            await self.asgi_app(scope, receive, send)

application = LifespanWrapper(application)
