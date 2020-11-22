from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Entry(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="journal_entries"
    )
    updated_on = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        self.title

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"pk": self.pk})
