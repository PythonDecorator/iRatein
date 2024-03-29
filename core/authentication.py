import jwt

from django.utils import timezone
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from app import settings  # noqa
from django.contrib.auth import get_user_model


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):

        token = request.COOKIES.get('jwt')

        if not token:
            return None

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:

            raise exceptions.AuthenticationFailed('unauthenticated')

        user = get_user_model().objects.get(pk=payload['user_id'])

        if user is None:
            raise exceptions.AuthenticationFailed('User not found!')

        return user, None

    @staticmethod
    def generate_jwt(user_id):
        payload = {
            'user_id': user_id,
            'exp': timezone.now() + timezone.timedelta(days=1),
            'iat': timezone.now(),
        }

        return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
