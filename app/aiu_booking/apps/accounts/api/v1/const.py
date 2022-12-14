from django.utils.translation import gettext_lazy as _


class SuccessResponseMessages:
    SIGNED_OUT = _("Successfully Sign out")


class ErrorResponseMessages:
    TOKEN_BLACKLISTED = _("Given Token is BlackList")


SRM = SuccessResponseMessages()
ERM = ErrorResponseMessages()
