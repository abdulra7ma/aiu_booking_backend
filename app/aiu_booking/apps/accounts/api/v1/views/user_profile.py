from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from aiu_booking.apps.accounts.api.v1.serializers.user_profile import (
    UserProfileSerializer, UserProfileUpdateSerializer
)


class UserProfileAPIView(RetrieveUpdateAPIView):

    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return UserProfileUpdateSerializer
        return super().get_serializer_class()

    def get_object(self):
        return self.request.user
