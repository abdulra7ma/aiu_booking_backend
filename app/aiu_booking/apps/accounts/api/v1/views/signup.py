from rest_framework import status
from rest_framework.generics import GenericAPIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from aiu_booking.apps.accounts.api.v1.serializers.registration import (
    RegistrationSerializer,
)
from aiu_booking.apps.accounts.services.signup import SignUpService


class SignUpAPIView(GenericAPIView):
    serializer_class = RegistrationSerializer
    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(
        responses={status.HTTP_204_NO_CONTENT: openapi.Response("")}
    )
    def post(self, request):
        service = SignUpService()
        return service.signup(request, self.get_serializer_class())
