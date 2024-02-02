import random

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from faker import Faker
from core.models import Message, ChatRoom


def create_user(email, first_name, last_name, password="testPass123"):
    """Create and return a new user."""
    return get_user_model().objects.create_user(email=email,
                                                password=password,
                                                first_name=first_name,
                                                last_name=last_name)


def create_chat_room(creator, users, room_name):
    """Create and return a chat room."""
    data = {
        'creator': creator,
        "room_name": room_name
    }

    chat_room = ChatRoom.objects.create(**data)
    for n in range(random.randrange(3, 6)):
        chat_room.members.add(random.choice(users))
        chat_room.save()
    return chat_room


def create_message(sender, receiver, content, room_name):
    """Create and return a message."""
    data = {
        'sender': sender,
        'receiver': receiver,
        "content": content,
        "room_name": room_name
    }

    message = Message.objects.create(**data)
    return message


class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()

        creator = get_user_model().objects.get(email="admin@example.com")

        users = [create_user(email=faker.email(),
                             first_name=faker.name(),
                             last_name=faker.name()
                             ) for _ in range(10)]
        room_name = create_chat_room(creator, users, "chat")

        for _ in range(40):
            create_message(sender=creator, receiver=random.choice(users),
                           content=faker.text(random.randrange(10, 100)),
                           room_name=room_name
                           )
