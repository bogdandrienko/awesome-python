from django.contrib import admin
from django_app import models


# Register your models here.

admin.site.register(models.Room)
admin.site.register(models.Message)
admin.site.register(models.ChatNotification)
admin.site.register(models.Notification)
