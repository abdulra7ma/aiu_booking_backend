from django.db import models
from django.utils.translation import gettext_lazy as _

from aiu_booking.apps.common.models.core import CoreModel


class Facility(CoreModel):
    name = models.CharField(_("Facility"), max_length=256)
    bio = models.TextField(_("Facility Bio"))
    image = models.FileField(
        upload_to="facilities",
        blank=True,
        default="facilities/default_facility.png",
    )
