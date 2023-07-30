from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    patient = models.ForeignKey(User, related_name="room_patient", on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(User, related_name="room_doctor", on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'django_app'
        ordering = ("name",)
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'
        # db_table = 'django_app_model_table'

    def __str__(self):
        return f"{self.name[:30]} {self.slug[:30]}"


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    message = models.TextField()
    data_added = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'django_app'
        ordering = ("-data_added",)
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        # db_table = 'django_app_model_table'

    def __str__(self):
        return f"{self.room.name} {self.user.username} [{self.data_added}] {self.message[:30]}"


class ChatNotification(models.Model):
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    message = models.TextField()
    is_seen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, default="")
    notification_place = models.CharField(max_length=300, default="")
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'django_app'
        ordering = ("-created_at",)
        verbose_name = 'Уведомления'
        verbose_name_plural = 'Уведомления'
        # db_table = 'django_app_model_table'
