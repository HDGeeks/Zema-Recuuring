from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "mandate": reverse(
                "mandate-list", request=request, format=format
            ),
             "transaction": reverse(
                "transaction-list", request=request, format=format
            ),
             "admin-site": reverse("admin:login", request=request, format=format),
            # doc
            "swagger-api-doc": reverse(
                "schema-swagger-ui", request=request, format=format
            ),
            "redoc-api-doc": reverse("schema-redoc", request=request, format=format),
            
        }
    )