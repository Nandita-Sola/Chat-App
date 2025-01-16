from django.urls import re_path
#from .consumers import ChatConsumer
from . import consumers

# Define WebSocket URL patterns for the chat application
websocket_urlpatterns = [
    #re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),  # URL pattern for WebSocket
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
