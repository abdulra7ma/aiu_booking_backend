from rest_framework.exceptions import APIException


def get_query_id(request, model_name: str) -> int:
    """Get an object id from the query params and validate the object id"""

    query_params = request.query_params

    if "id" not in query_params:
        raise APIException(
            detail=f"{model_name} id not specified in the query params",
            code=f"{model_name.lower()}_query_id_not_found",
        )

    if query_params["id"] == "":
        raise APIException(
            detail=f"{model_name} id not specified in the query params",
            code=f"{model_name.lower()}_query_id_not_found",
        )

    return query_params["id"]
