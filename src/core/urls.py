from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static

from drf_yasg import openapi
from django.conf import settings



schema_view = get_schema_view(
    # API schema for our accounts
    openapi.Info(
        title="Recurring API",
        default_version="v1",
        description="Recurring API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="dannyhd88@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("recur/", include("recurring.urls")),
    
    # API documentation urls
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("openapi.yml", schema_view.without_ui(cache_timeout=0), name="schema-json"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

