from django.shortcuts import render

# Create your views here.
"""
def chat_room(request, room_name):
    return render(request, 'chat/chat.html', {
        'room_name': room_name
    })

def index(request):
    return render(request, 'chat/index.html')  # Render the 'chat/index.html' template
"""
def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })