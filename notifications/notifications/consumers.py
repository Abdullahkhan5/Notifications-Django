# your_app_name/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket connected")  # Add this for debugging
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        print("WebSocket disconnected")  # Add this for debugging
        await self.channel_layer.group_discard("notifications", self.channel_name)

    async def send_notification(self, event):
        print(f"Sending notification: {event['message']}")  # Add this for debugging
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))
