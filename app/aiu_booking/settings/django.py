from pathlib import Path

from .environment import env

BASE_DIR = Path(__file__).resolve().parent.parent


def rel(*path):
    return BASE_DIR.joinpath(*path)


DEBUG = env.bool("AIU_BOOKING_DEBUG", default=False)

INTERNAL_IPS = env.list("AIU_BOOKING_INTERNAL_IPS", default=[])

ALLOWED_HOSTS = env.list("AIU_BOOKING_ALLOWED_HOSTS", default=[])

SECRET_KEY = env.str("AIU_BOOKING_SECRET_KEY")

INSTALLED_APPS = [
    # django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party apps
    "rest_framework",
    "django_extensions",
    "django_filters",
    "drf_yasg",
    "rest_framework_simplejwt.token_blacklist",
    # our apps
    "aiu_booking.apps.common",
    "aiu_booking.apps.accounts",
    "aiu_booking.apps.booking",
] + env.list("AIU_BOOKING_DEV_INSTALLED_APPS", default=[])

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
] + env.list("AIU_BOOKING_DEV_MIDDLEWARE", default=[])

ROOT_URLCONF = "aiu_booking.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [rel("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "aiu_booking.wsgi.application"

DATABASES = {
    "default": env.db(
        "AIU_BOOKING_DATABASE_URL",
        default="psql://postgres:awesome_password_1@database:5432/aiu_booking_db",
    )
}

AUTH_USER_MODEL = "accounts.UserAccount"
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]

SECURE_BROWSER_XSS_FILTER = env.bool(
    "AIU_BOOKING_SECURE_BROWSER_XSS_FILTER", default=True
)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "AIU_BOOKING_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)
SESSION_COOKIE_HTTPONLY = env.bool(
    "AIU_BOOKING_SESSION_COOKIE_HTTPONLY", default=True
)
SESSION_COOKIE_SECURE = env.bool(
    "AIU_BOOKING_SESSION_COOKIE_SECURE", default=True
)
CSRF_COOKIE_SECURE = env.bool("AIU_BOOKING_CSRF_COOKIE_SECURE", default=True)
X_FRAME_OPTIONS = env.str("AIU_BOOKING_X_FRAME_OPTIONS", default="SAMEORIGIN")
SECURE_HSTS_SECONDS = env.int(
    "AIU_BOOKING_SECURE_HSTS_SECONDS", default=31536000
)  # 1 year
SESSION_COOKIE_NAME = "s"
CSRF_COOKIE_NAME = "c"

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [rel("..", "..", "app", "locale")]

STATIC_URL = env.str("AIU_BOOKING_STATIC_URL", default="/s/")
STATIC_ROOT = env.str(
    "AIU_BOOKING_STATIC_ROOT", default=rel("..", "..", "public", "static")
)

MEDIA_URL = env.str("AIU_BOOKING_MEDIA_URL", default="/m/")
MEDIA_ROOT = env.str(
    "AIU_BOOKING_MEDIA_ROOT", rel("..", "..", "public", "media")
)

EMAIL_BACKEND = env.str(
    "AIU_BOOKING_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
if (
    EMAIL_BACKEND == "django.core.mail.backends.smtp.EmailBackend"
):  # pragma: no cover
    EMAIL_HOST = env.str("AIU_BOOKING_EMAIL_HOST")
    EMAIL_PORT = env.str("AIU_BOOKING_EMAIL_PORT")
    EMAIL_HOST_USER = env.str("AIU_BOOKING_EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = env.str("AIU_BOOKING_EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = env.bool("AIU_BOOKING_EMAIL_USE_TLS", default=True)

SITE_ID = env.int("AIU_BOOKING_SITE_ID", default=1)

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

APPEND_SLASH = False

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
