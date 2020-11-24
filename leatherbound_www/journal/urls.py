from django.urls import path
from . import views


urlpatterns = [
    path("api/entry/", views.EntryList.as_view(), name="home"),
    path("api/entry/<uuid>/", views.EntryDetail.as_view(), name="entry_detail"),
    #path("user/", views.UserList.as_view()),
    path("api/user/<pk>/", views.UserDetail.as_view()),
    path("api/register/", views.CreateUserView.as_view()),
]
