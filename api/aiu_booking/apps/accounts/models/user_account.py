from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy

from aiu_booking.apps.common import models as core_models
from aiu_booking.apps.common.models import CoreModel


class UserManager(core_models.CoreManager, BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must give an email address")

        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class UserAccount(PermissionsMixin, CoreModel, AbstractBaseUser):

    email = models.EmailField(verbose_name=gettext_lazy("email address"), unique=True)
    student_id = models.CharField(verbose_name=gettext_lazy("Student ID"), unique=True, max_length=128)
    is_staff = models.BooleanField(
        gettext_lazy("staff status"),
        default=False,
        help_text=gettext_lazy("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        gettext_lazy("active"),
        default=True,
        help_text=gettext_lazy(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_short_name(self) -> str:
        return str(self.email)

    def get_student_id(self):
        if not self.student_id:
            return self.get_short_name()
        return self.student_id

    @property
    def notification_salutation(self):
        if self.student_id:
            salutation = f"{self.student_id}"
        else:
            salutation = gettext_lazy("Dear client")
        return salutation
