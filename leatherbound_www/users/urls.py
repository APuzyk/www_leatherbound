from django.urls import path
from . import views


urlpatterns = [
    path('api/register/', views.UserRegister.as_view(), name='register'),
]
