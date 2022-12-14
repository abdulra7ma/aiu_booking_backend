from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from aiu_booking.apps.accounts.api.v1.const import SRM, ERM
from aiu_booking.apps.accounts.api.v1.serializers.user_profile import (
    UserProfileSerializer,
)


class SignInService:
    @classmethod
    def signin(cls, request, serializer):
        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get("user")

        # generate account access token
        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token

        return Response(
            data={
                "tokens": {
                    "access": str(access_token),
                    "refresh": str(refresh_token),
                },
                "user": UserProfileSerializer(instance=user).data,
            },
            status=status.HTTP_201_CREATED,
        )


class SignOutService:
    @staticmethod
    def sign_out(request, serializer):
        """
        Logout a user by blacklisting his refresh token. This view needs to
        receive a refresh token in order to blacklist it, so it will not be
        valid to be used anymore.
        """

        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            token = RefreshToken(serializer.data["token"])
            token.blacklist()
        except TokenError as e:
            # if the token is blacklisted than it will raise TokenError.
            return Response(
                str(e),
                status=status.HTTP_400_BAD_REQUEST,
                status_message=ERM.TOKEN_BLACKLISTED,
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            status_message=SRM.SIGNED_OUT,
        )
