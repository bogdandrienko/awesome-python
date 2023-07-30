from django.urls import path
from django_app import consumers

websocket_urlpatterns = [
    # path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    # path('ws/notifications/', consumers.ChatConsumer.as_asgi()),
    # path('websocket/notifications/<str:user_name>/', consumers.NotificationConsumer.as_asgi()),
    path('ws/site_notifications/<int:user_id>/', consumers.NotificationConsumer.as_asgi()),
    # path('websocket/chat_notifications/<int:user_id>/', consumers.ChatNotificationConsumer.as_asgi()),
    # path('ws/notify/', consumers.ChatNotificationConsumer)
]
