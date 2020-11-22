# Generated by Django 3.1.2 on 2020-11-08 01:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0006_auto_20201107_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]