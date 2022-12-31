from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)

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
