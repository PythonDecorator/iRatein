import random

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from faker import Faker
from core.models import Category, Server, Channel  # noqa


def create_user(email, first_name, last_name, password="testPass123"):
    """Create and return a new user."""
    return get_user_model().objects.create_user(email=email,
                                                password=password,
                                                first_name=first_name,
                                                last_name=last_name)


def create_category(name, text):
    """Create and return a category."""
    data = {
        'name': name,
        'description': text,
    }

    category = Category.objects.create(**data)
    return category


def create_server(owner, category, users, n):
    """Create and return a server."""
    data = {
        'name': f'Server_{n}',
        'description': 'This is just a sample server',
        "owner": owner,
        "category": category,
    }

    server = Server.objects.create(**data)
    for n in range(random.randrange(3, 6)):
        server.members.add(random.choice(users))
        server.save()
    return server


def create_channel(owner, category, server, n):
    """Create and return a channel."""
    data = {
        'name': 'Sample Server',
        'topic': f'Topic_{n}',
        "owner": owner,
        "category": category,
        "server": server
    }

    channel = Channel.objects.create(**data)
    return channel


class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()

        create_user(email="test@example.com",
                    first_name="Test",
                    last_name="Name",
                    password="aaaaaaaa"
                    )
        for n in range(1, 10):
            create_user(email=faker.email(),
                        first_name=faker.name(),
                        last_name=faker.name()
                        )

        for n in range(1, 100):
            users = get_user_model().objects.all()
            user = random.choice(users)

            category = create_category(
                name=faker.name(),
                text=faker.text(50)
            )

            server = create_server(
                owner=user,
                category=category,
                n=n,
                users=users
            )

            create_channel(owner=user, category=category, server=server, n=n)
