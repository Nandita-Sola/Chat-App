"""
ASGI config for chatapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

# chatapp/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat import routing
#from chat import urls  # Import WebSocket routing from chat/urls.py

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP protocol (regular Django views)
    "websocket": AuthMiddlewareStack(
        URLRouter(
            #urls.websocket_urlpatterns  # Add WebSocket URL routing here
            routing.websocket_urlpatterns
        )
    ),
})

