import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async, async_to_sync
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from django_app import models
from django_app import serializers


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Присоединяемся к комнате уведомлений пользователя
        self.user_id = int(self.scope["url_route"]["kwargs"]["user_id"])
        # self.user = self.scope['user']
        # self.user = User.objects.get(username=self.username)
        # print(self.username)
        # print(self.user)
        print(self.user_id)
        # self.room_group_name = f'notification_{self.username}'
        self.room_group_name = f'notification_{self.user_id}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Отсоединяемся от комнаты уведомлений пользователя
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Этот метод не используется в данном случае,
        # потому что мы отправляем данные только с сервера на клиент
        pass

    async def send_notification(self, event):
        # Метод для отправки уведомлений на клиент
        notification = event['notification']
        await self.send(text_data=json.dumps({
            'notification': serializers.NotificationSerializer(notification).data
        }))

# class NotificationConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         user_id = self.scope['user'].id
#         print(user_id)
#         self.notification_group_name = f'user_{user_id}'
#         await self.channel_layer.group_add(
#             self.notification_group_name,
#             self.channel_name
#         )
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.notification_group_name,
#             self.channel_name
#         )
#
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         notification_text = text_data_json['notification_text']
#
#         await self.channel_layer.group_send(
#             self.notification_group_name,
#             {
#                 'type': 'send_notification',
#                 'text': notification_text
#             }
#         )
#
#     async def send_notification(self, event):
#         notification_text = event['text']
#
#         await self.send(text_data=json.dumps({
#             'notification_text': notification_text
#         }))