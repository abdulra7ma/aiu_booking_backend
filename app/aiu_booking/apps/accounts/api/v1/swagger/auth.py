from drf_yasg import openapi


sign_out_token = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["token"],
    properties={
        "token": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Refresh Toke",
            example="<user refresh token>",
        ),
    },
)
