from channels.generic.websocket import AsyncWebsocketConnection
import json

class ChatConsumers(AsyncWebsocketConnection):
    async def connect(self):
        await self.accept()
    
    async def receive(self,message):
        data = json.loads(message)

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.parking_group_name,
            self.channel_name
        )

