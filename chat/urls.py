from django.urls import path, re_path
from . import consumers
from . import views

# Regular HTTP routes (for example, the index or home page)

urlpatterns = [
    path('', views.index, name='index'),  # Home page route
    path('<str:room_name>/', views.room, name='room'),  # Chat room route
]

# WebSocket URL patterns (make sure to include these as well)
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),  # WebSocket URL for chat rooms
]

app_name = 'chat'