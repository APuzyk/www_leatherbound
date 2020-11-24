"""leatherbound URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/api-token-auth/', views.obtain_auth_token),
    path('', include('journal.urls')),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/users/', include("django.contrib.auth.urls")),
    path('api/users/', include("users.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
