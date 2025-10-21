from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# Schema view for API documentation
schema_view = get_schema_view(
openapi.Info(
title="Student Management API",
default_version='v1',

description="API documentation for Student Management System",
terms_of_service="https://www.google.com/policies/terms/",
contact=openapi.Contact(email="contact@example.com"),
license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
# Admin site
path('admin/', admin.site.urls),
# API endpoints
path('api/', include('students.urls')),
# API Documentation - Swagger UI
path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
name='schema-swagger-ui'),

# API Documentation - ReDoc
path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
name='schema-redoc'),

# API Documentation - JSON format
path('swagger.json', schema_view.without_ui(cache_timeout=0),
name='schema-json'),
# API Documentation - YAML format
path('swagger.yaml', schema_view.without_ui(cache_timeout=0),
name='schema-yaml'),
]