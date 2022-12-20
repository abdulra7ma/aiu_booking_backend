from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from aiu_booking.apps.accounts.api.v1.serializers.user_profile import UserProfileSerializer
from aiu_booking.apps.accounts.selectors.account import get_user_by_email


class SignUpService:
    @classmethod
    def signup(cls, request, serializer):
        data = request.data

        serializer = serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # get serialized email data
        email = serializer.validated_data["email"]

        # get the new created user and activate it
        user = get_user_by_email(email=email)

        # activate the new registered user
        # user.is_active = True
        # user.save()

        print(user)

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
