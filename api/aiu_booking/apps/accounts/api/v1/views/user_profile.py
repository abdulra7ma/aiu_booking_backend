from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from aiu_booking.apps.accounts.api.v1.serializers.user_profile import UserProfileSerializer


class UserProfileAPIView(RetrieveUpdateAPIView):

    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
