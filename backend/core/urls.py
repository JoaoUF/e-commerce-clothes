from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view # type: ignore
from drf_yasg import openapi # type: ignore

schema_view = get_schema_view(
   openapi.Info(
      title="Clothes-Ecommerce",
      default_version='v1',
      description="API Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="jurrunagaf@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.msproduct.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
