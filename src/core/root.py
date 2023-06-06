from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from urllib.parse import urljoin




# @api_view(["GET"])
# def api_root(request, format=None):
#     return Response(
#         {
#             "create-mandate": reverse("mandate-list", request=request, format=format),
#             "transaction": reverse("transaction-list", request=request, format=format),
#             "admin-site": reverse("admin:login", request=request, format=format),
#             # doc
#             "swagger-api-doc": reverse(
#                 "schema-swagger-ui", request=request, format=format
#             ),
#             "redoc-api-doc": reverse("schema-redoc", request=request, format=format),
#         }
#     )



@api_view(["GET"])
def api_root(request, format=None):
    urls = {
        "create-mandate": urljoin(reverse("mandate-list", request=request, format=format), "196.189.126.147"),
        "transaction": urljoin(reverse("transaction-list", request=request, format=format), "196.189.126.147"),
        "admin-site": urljoin(reverse("admin:login", request=request, format=format), "196.189.126.147"),
        # doc
        "swagger-api-doc": urljoin(reverse("schema-swagger-ui", request=request, format=format), "196.189.126.147"),
        "redoc-api-doc": urljoin(reverse("schema-redoc", request=request, format=format), "196.189.126.147"),
    }

    return Response(urls)
