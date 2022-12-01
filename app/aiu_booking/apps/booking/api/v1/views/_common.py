from rest_framework.mixins import DestroyModelMixin

from drf_rw_serializers.generics import GenericAPIView
from drf_rw_serializers.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)


class CoreCRUDAPIVIew(
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericAPIView,
):
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().update(request, *args, partial=True, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
