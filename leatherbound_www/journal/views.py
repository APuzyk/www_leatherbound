# from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwner, IsUser
from .serializers import EntrySerializer
from .models import Entry
from datascience.calls import runEntryModels
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            #'users': reverse('user-list', request=request, format=format),
            "entries": reverse("entry-list", request=request, format=format)
        }
    )


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUser, IsAuthenticated]


class CreateUserView(generics.CreateAPIView):

    model = User
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [IsOwner, IsAuthenticated]

    def perform_create(self, serializer):
        entry = serializer.save(author=self.request.user)
        runEntryModels(entry)

    def get_queryset(self):
        user = self.request.user
        return Entry.objects.filter(author=user).order_by('-created_on')


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = EntrySerializer
    lookup_field = "uuid"
