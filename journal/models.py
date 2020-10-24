from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Entry(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="journal_entries"
    )
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        self.title

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})
