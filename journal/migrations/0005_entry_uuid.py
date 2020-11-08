# Generated by Django 3.1.2 on 2020-11-08 01:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_remove_entry_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]
