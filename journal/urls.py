from django.urls import path
from . import views


urlpatterns = [
    path("", views.EntryList.as_view(), name="home"),
    path("entry/<pk>/", views.EntryDetail.as_view(), name="entry_detail"),
    path("create/", views.EntryCreate.as_view(), name="entry_create"),
    path("entry/<pk>/edit", views.EntryEdit.as_view(), name="entry_edit"),
    path("entry/<pk>/delete", views.EntryDelete.as_view(), name="entry_delete"),
]
