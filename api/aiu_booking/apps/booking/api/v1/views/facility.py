from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from aiu_booking.apps.booking.api.v1.serializers.facility import (
    FacilityCreateSerializer,
    FacilitySerializer,
)
from aiu_booking.apps.booking.models.facility import Facility
from aiu_booking.apps.booking.utils.request import get_query_id
from aiu_booking.apps.booking.utils.swagger.facility import facility_id_param


class FacilityAPIView(
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericAPIView,
):
    def get_object(self):
        facility_id = get_query_id(self.request, _("Facility"))

        try:
            return Facility.objects.get(id=facility_id)
        except ObjectDoesNotExist:
            raise APIException(_("Facility not found"))

    @swagger_auto_schema(
        manual_parameters=[facility_id_param],
        tags=["facility"],
        responses={
            status.HTTP_200_OK: openapi.Response(
                "Facility response object",
                schema=FacilitySerializer,
            )
        },
    )
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                "Facility response object",
                schema=FacilitySerializer,
            )
        },
        request_body=FacilityCreateSerializer,
        tags=["facility"],
    )
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={status.HTTP_201_CREATED: openapi.Response("")},
        request_body=FacilityCreateSerializer,
        manual_parameters=[facility_id_param],
        tags=["facility"],
    )
    def patch(self, request, *args, **kwargs):
        return super().update(request, *args, partial=True, **kwargs)

    @swagger_auto_schema(
        manual_parameters=[facility_id_param], tags=["facility"]
    )
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method in ["POST", "PATCH"]:
            return FacilityCreateSerializer
        return FacilitySerializer
