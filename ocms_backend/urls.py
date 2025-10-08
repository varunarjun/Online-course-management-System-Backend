from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# -----------------------------
# Home page
# -----------------------------
def home(request):
    return JsonResponse({"message": "Welcome to OCMS. Use /swagger/ to explore APIs."})

# -----------------------------
# Swagger Info
# -----------------------------
swagger_info = openapi.Info(
    title="OCMS API",
    default_version='v1',
    description="Online Course Management System API Documentation",
    terms_of_service="https://www.example.com/terms/",
    contact=openapi.Contact(email="support@example.com"),
    license=openapi.License(name="MIT License"),
)

# -----------------------------
# Schema view
# -----------------------------
schema_view = get_schema_view(
    swagger_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# -----------------------------
# URL Patterns
# -----------------------------
urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Home
    path('', home, name='home'),

    # App URLs
    path('api/users/', include('users.urls')),
    path('api/courses/', include('courses.urls')),
    path('api/enrollments/', include('enrollments.urls')),

    # JWT Auth URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger.yaml', schema_view.without_ui(cache_timeout=0), name='schema-yaml'),
]
