import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.renderers import JSONRenderer

from core.serializers import MessageSerializer
from core.models import User, ChatRoom, Message


@database_sync_to_async
def new_message_query(user, room_name, data):
    user = User.objects.get(email=user.email)
    content = data.get("message")
    room_name, created = ChatRoom.objects.get_or_create(room_name=room_name)
    massage_model = Message.objects.create(sender=user,
                                           content=content,
                                           room_name=room_name)
    print(massage_model.sender)
    return massage_model


@database_sync_to_async
def get_chat_room(room_name):
    return ChatRoom.objects.get(room_name=room_name)


@database_sync_to_async
def clear_history_query(room_name):
    try:
        chat_room_messages = Message.objects.filter(chat_room__room_name=room_name)
        chat_room_messages.delete()
        return True
    except Exception as e:
        print(e)
        return False


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.user = None
        self.room_name = None
        self.room_group_name = None
        self.commands = {
            'message_created': self.message_created,
        }

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        self.user = self.scope['user']

        # Join room group
        if self.user.is_authenticated:
            await self.channel_layer.group_add(
                self.room_group_name, self.channel_name
            )
            await self.accept()
        else:
            await self.disconnect(403)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            text_data_dict = json.loads(text_data)
            command = text_data_dict['command']
            await self.commands[command](text_data_dict)

    async def message_created(self, data):
        create_new_message = await new_message_query(self.user, self.room_name, data)
        new_message_json = await self.message_serializer(create_new_message)
        result = eval(new_message_json)  # REMOVE BYTE STRING

        context = {'command': 'message_created', 'result': result}
        await self.send_message_to_chat_room(context)

    @staticmethod
    async def message_serializer(query):
        serialized_message = MessageSerializer(query)
        message_json = JSONRenderer().render(serialized_message.data)
        return message_json

    async def send_message_to_chat_room(self, data):

        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat.message",
                "message": data["result"]["content"]})

    async def chat_message(self, event):
        message = event["message"]

        await self.send(text_data=json.dumps({"message": message}))
