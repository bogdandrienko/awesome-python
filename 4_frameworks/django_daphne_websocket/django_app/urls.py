from django.contrib import admin
from django.urls import path, include
from django_app import views

urlpatterns = [
    # path('', views.index),
    path('', views.notification, name='notification'),
    # path('get_connected_websockets/', views.get_connected_websockets, name='get_connected_websockets'),
    # path('rooms/', views.rooms, name='rooms'),
    path('example/', views.example, name='example'),
    # path('<slug:slug>/', views.room, name='room'),
]
