from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from aiu_booking.apps.accounts.api.permissions import IsNotAuthenticated
from aiu_booking.apps.accounts.api.v1.serializers.auth.signin import SignInSerializer
from aiu_booking.apps.accounts.api.v1.serializers.auth.signout import SignOutRefreshTokenSerializer
from aiu_booking.apps.accounts.api.v1.swagger.auth import sign_out_token
from aiu_booking.apps.accounts.services.signin import SignInService, SignOutService


class SignInAPIView(GenericAPIView):
    permission_classes = [IsNotAuthenticated]
    serializer_class = SignInSerializer

    @swagger_auto_schema(
        responses={status.HTTP_204_NO_CONTENT: openapi.Response("")}
    )
    def post(self, request):
        response = SignInService.signin(request, self.get_serializer_class())
        return response


class SignOutView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SignOutRefreshTokenSerializer

    @swagger_auto_schema(
        responses={status.HTTP_204_NO_CONTENT: openapi.Response("")},
        request_body=sign_out_token,
    )
    def post(self, request):
        response = SignOutService.sign_out(request, self.get_serializer_class())
        return response
