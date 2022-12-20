from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.settings import api_settings


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        tokens = {
            "access": {
                "token": token["access"],
                "expire_date": api_settings.ACCESS_TOKEN_LIFETIME,
            },
            "refresh": {
                "token": token["refresh"],
                "expire_date": api_settings.REFRESH_TOKEN_LIFETIME,
            },
        }

        return tokens
