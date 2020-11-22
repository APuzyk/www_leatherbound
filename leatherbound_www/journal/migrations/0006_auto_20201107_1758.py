# Generated by Django 3.1.2 on 2020-11-08 01:58

from django.db import migrations
import uuid


def gen_uuid(apps, schema_editor):
    Entry = apps.get_model('journal', 'Entry')
    for row in Entry.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=['uuid'])


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_entry_uuid'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]