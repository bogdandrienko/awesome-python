import datetime
import time

from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.cache import caches
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render
from channels.layers import get_channel_layer
from channels.layers import InMemoryChannelLayer
from asgiref.sync import async_to_sync

from django_app import models

default_cache = caches['default']
MULTIPLY = 1.3

channel_layer = InMemoryChannelLayer()

def cache(key: str, function_queryset: any) -> any:
    result = default_cache.get(key)
    if result:
        return result
    result = function_queryset()
    default_cache.set(key, result, timeout=5 * MULTIPLY)
    return result


# Create your views here.


# def time_measure(func):
#     def wrapper(*args, **kwargs):
#         time_start = time.perf_counter()
#         result = func(*args, **kwargs)
#         print(f"time elapsed: {round(time.perf_counter() - time_start, 5)}")
#         return result
#
#     return wrapper


# @time_measure
# def index(request: HttpRequest) -> JsonResponse:
#     # for i in range(1, 10000):
#     #     User.objects.create(
#     #         username=f"user{i}",
#     #         password=make_password(f"user{i} Qwerty!", )
#     #     )
#
#     users_ins = cache(key="users_filter_active", function_queryset=lambda: User.objects.filter(is_active=True))
#     print(users_ins)
#     users_json = [{"username": f"{user.username}", "password": f"{user.password}", "email": f"{user.email}"}
#                   for user in users_ins]
#     print(users_json)
#
#     return JsonResponse(data=users_json, safe=False)


# @login_required
# def rooms(request):
#     return render(request, "django_app/rooms.html", {"rooms": models.Room.objects.all()})


# @login_required
# def room(request, slug):
#     room_obj = models.Room.objects.get(slug=slug)
#     messages = models.Message.objects.filter(room=room_obj)[:25]
#     rooms_users = room_obj.room_users.all()
#     list_of_users = [user.username for user in rooms_users if user != request.user]
#     return render(request, "django_app/room.html", {"room": room_obj, "messages": messages,
#                                                     "second_user": list_of_users[0], 'user_id': request.user.id})


@login_required
def notification(request):
    return render(request, "django_app/notification.html")


@login_required
def example(request):
    send_notification(request.user, "HI")
    return HttpResponse("Good")


def send_notification(user, message):
    # Создаем новое уведомление
    notification = models.Notification.objects.create(user=user, message=message)
    # Получаем канальный слой для отправки уведомлений
    channel_layer = get_channel_layer()
    # Отправляем уведомление клиенту через WebSocket
    # print(user.id)
    async_to_sync(channel_layer.group_send)(
        f'notification_{user.id}',
        # f'notification_{user.username}',
        {
            'type': 'send_notification',
            'notification': notification,
        }
    )


def get_connected_websockets_f():
    connected_websockets = async_to_sync(channel_layer.group_channels)("websocket.connect")
    return connected_websockets


def get_connected_websockets(request):
    # Использование
    connected_websockets = get_connected_websockets_f()
    print(connected_websockets)
    return HttpResponse("Good")


