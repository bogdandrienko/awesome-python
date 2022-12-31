from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room, Message


@login_required
def rooms(request):
    return render(request, 'django_app/rooms.html', {'rooms': Room.objects.all()})


@login_required
def room(request, slug):
    room_obj = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room_obj)[0:25]
    return render(request, 'django_app/room.html', {'room': room_obj, 'messages': messages})
