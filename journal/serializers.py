from . import models as m
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    entries = serializers.PrimaryKeyRelatedField(
        many=True, queryset=m.Entry.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "entries"]


class EntrySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = m.Entry
        fields = ["uuid", "title", "author", "updated_on", "content", "created_on"]
