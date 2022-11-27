from django.db import models
from aiu_booking.apps.common.models.core import CoreModel
from django.utils.translation import gettext_lazy as _


class Facility(CoreModel):
    name = models.CharField(_("Facility"), max_length=256)
    bio = models.TextField(_("Facility Bio"))
    image = models.FileField(upload_to="facilities", blank=True)
