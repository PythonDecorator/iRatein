# Generated by Django 3.2.23 on 2024-02-02 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_message_chat_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='chat_room',
            new_name='room_name',
        ),
    ]