from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    # Register new user
    path('register/', views.RegisterUserView.as_view(), name='users_register_create'),

    # Login user (custom view to return JWT + extra info)
    path('login/', views.login_user, name='users_login_create'),

    # Refresh JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='users_token_refresh_create'),
]
