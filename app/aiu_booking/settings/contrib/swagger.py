from ..environment import env


SWAGGER_SETTINGS = {
    "DEFAULT_API_URL": env.str(
        "AIU_BOOKING_BASE_API_URL", default="https://api.aiu_booking.com"
    ),
}
