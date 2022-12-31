from django.contrib import admin
from django.urls import path, include
from django_app import views

urlpatterns = [
    # path('', views.index),
    path('', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
]
