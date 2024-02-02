"""
Serializers for the user API View.
"""
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers

from core.models import Message, User

from .models import Message, ChatRoom
from collections import OrderedDict


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='name', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='name', queryset=User.objects.all())

    def to_representation(self, instance):
        # this function will remove keys that have None value
        result = super(MessageSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'content', 'timestamp']


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ["id", 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {"password": {"write_only": True,
                                     "min_length": 8}
                        }

    def create(self, validated_data):
        """Create and return a user with encrypted password."""

        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return a user with encrypted password."""

        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ["id", 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {"password": {"write_only": True, "min_length": 8},
                        "email": {"read_only": True},
                        "id": {"read_only": True}
                        }


class AuthTokenSerializer(serializers.Serializer):  # noqa
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )

        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
