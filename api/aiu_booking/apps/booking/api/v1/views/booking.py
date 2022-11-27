from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import APIException
from rest_framework import status

from aiu_booking.apps.booking.api.v1.serializers.booking import (
    BookingCreateSerializer,
    BookingSerializer,
)
from aiu_booking.apps.booking.models.booking import Booking
from aiu_booking.apps.booking.utils.request import get_query_id
from aiu_booking.apps.booking.utils.swagger.booking import booking_id_param

from ._common import CoreCRUDAPIVIew

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class BookingAPIView(CoreCRUDAPIVIew):
    read_serializer_class = BookingCreateSerializer
    write_serializer_class = BookingSerializer

    def get_object(self):
        booking_id = get_query_id(self.request, _("Booking"))

        try:
            return Booking.objects.get(id=booking_id)
        except ObjectDoesNotExist:
            raise APIException(_("Booking not found"))

    @swagger_auto_schema(
        manual_parameters=[booking_id_param],
        tags=["booking"],
        responses={
            status.HTTP_200_OK: openapi.Response(
                "Booking response object",
                schema=BookingSerializer,
            )
        },
    )
    def get(self, request, *args, **kwargs):
        return super(BookingAPIView, self).get(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                "Booking response object",
                schema=BookingSerializer,
            )
        },
        request_body=BookingCreateSerializer,
        tags=["facility"],
    )
    def post(self, request, *args, **kwargs):
        return super(BookingAPIView, self).post(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                "Booking response object", schema=BookingSerializer
            )
        },
        request_body=BookingCreateSerializer,
        manual_parameters=[booking_id_param],
        tags=["booking"],
    )
    def patch(self, request, *args, **kwargs):
        return super(BookingAPIView, self).update(
            request, *args, partial=True, **kwargs
        )

    @swagger_auto_schema(
        manual_parameters=[booking_id_param], tags=["booking"]
    )
    def delete(self, request, *args, **kwargs):
        return super(BookingAPIView, self).delete(request, *args, **kwargs)
