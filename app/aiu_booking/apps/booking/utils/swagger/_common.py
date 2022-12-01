from uuid import uuid4

from drf_yasg import openapi


def get_query_id_param(desc):
    return openapi.Parameter(
        "id",
        in_=openapi.IN_QUERY,
        description=desc,
        type=openapi.TYPE_STRING,
        required=False,
        default=str(uuid4()),
    )
