from django.db import models

# Create your models here.

# chat/models.py
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message[:50]}'
