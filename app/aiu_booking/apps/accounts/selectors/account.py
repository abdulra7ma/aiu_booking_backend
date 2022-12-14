from aiu_booking.apps.accounts.models.user_account import UserAccount
from django.core.exceptions import ObjectDoesNotExist


def get_user_by_email(email: str):
    """
    Get user account by email
    """
    try:
        return UserAccount.objects.get(email=email)
    except ObjectDoesNotExist:
        return None
