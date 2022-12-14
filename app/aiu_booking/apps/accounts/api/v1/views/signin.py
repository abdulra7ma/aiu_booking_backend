from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from aiu_booking.apps.accounts.api.permissions import IsNotAuthenticated
from aiu_booking.apps.accounts.api.v1.serializers.login import LoginSerializer
from aiu_booking.apps.accounts.services.signin import SignInService


class SignInAPIView(GenericAPIView):
    permission_classes = [IsNotAuthenticated]
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        responses={status.HTTP_204_NO_CONTENT: openapi.Response("")}
    )
    def post(self, request):
        response = SignInService.signin(request, self.get_serializer_class())
        return response


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={status.HTTP_204_NO_CONTENT: openapi.Response("")}
    )
    def post(self, request):
        response = SignInService.logout(request)
        return response
