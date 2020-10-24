from django.urls import path
from . import views


urlpatterns = [
    path("", views.EntryList.as_view(), name="home"),
    path("entry/<slug:slug>/", views.EntryDetail.as_view(), name="entry_detail"),
    path("create/", views.EntryCreate.as_view(), name="entry_create"),
    path("entry/<slug:slug>/edit", views.EntryEdit.as_view(), name="entry_edit"),
    path("entry/<slug:slug>/delete", views.EntryDelete.as_view(), name="entry_delete"),
]
