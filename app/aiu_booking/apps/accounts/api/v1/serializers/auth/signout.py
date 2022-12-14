import jwt
from django.conf import settings
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.exceptions import InvalidToken


class SignOutRefreshTokenSerializer(Serializer):
    token = serializers.CharField(required=True)

    @staticmethod
    def validate_token(token):
        try:
            payload = jwt.decode(
                jwt=token,
                key=settings.SECRET_KEY,
                algorithms=["HS256"],
            )
        except jwt.ExpiredSignatureError as e:
            raise InvalidToken("Token expired", code="token_expired")
        except jwt.exceptions.DecodeError as e:
            raise InvalidToken("Invalid token", code="invalid_token")
        return payload
