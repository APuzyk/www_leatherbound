from django.urls import path
from . import views


urlpatterns = [
    path("entry/", views.EntryList.as_view(), name="home"),
    path("entry/<uuid>/", views.EntryDetail.as_view(), name="entry_detail"),
    #path("user/", views.UserList.as_view()),
    path("user/<pk>/", views.UserDetail.as_view()),
    path("register/", views.CreateUserView.as_view()),
]
