

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse





@api_view(["GET"])
def prod_root(request, format=None):
    return Response(
        {
    "create-mandate": "http://196.189.126.147/recur/create-mandate",
    "transaction": "http://196.189.126.147/recur/transaction",
    "admin-site": "http://196.189.126.147/admin/login/",
    "swagger-api-doc": "http://196.189.126.147/swagger/",
    "redoc-api-doc": "http://196.189.126.147/redoc/"
    "redoc-api-doc-test": "http://196.189.126.147/redoc/"
}
    )
