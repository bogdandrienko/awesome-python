import datetime
import time

from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.cache import caches
from django.http import JsonResponse, HttpRequest
from django.shortcuts import render

from django_app import models

default_cache = caches['default']
MULTIPLY = 1.3


def cache(key: str, function_queryset: any) -> any:
    result = default_cache.get(key)
    if result:
        return result
    result = function_queryset()
    default_cache.set(key, result, timeout=5 * MULTIPLY)
    return result


# Create your views here.


def time_measure(func):
    def wrapper(*args, **kwargs):
        time_start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"time elapsed: {round(time.perf_counter() - time_start, 5)}")
        return result

    return wrapper


@time_measure
def index(request: HttpRequest) -> JsonResponse:
    # for i in range(1, 10000):
    #     User.objects.create(
    #         username=f"user{i}",
    #         password=make_password(f"user{i} Qwerty!", )
    #     )

    users_ins = cache(key="users_filter_active", function_queryset=lambda: User.objects.filter(is_active=True))
    print(users_ins)
    users_json = [{"username": f"{user.username}", "password": f"{user.password}", "email": f"{user.email}"}
                  for user in users_ins]
    print(users_json)

    return JsonResponse(data=users_json, safe=False)


@login_required
def rooms(request):
    return render(request, "django_app/rooms.html", {"rooms": models.Room.objects.all()})


@login_required
def room(request, slug):
    room_obj = models.Room.objects.get(slug=slug)
    messages = models.Message.objects.filter(room=room_obj)[:25]
    return render(request, "django_app/room.html", {"room": room_obj, "messages": messages})
