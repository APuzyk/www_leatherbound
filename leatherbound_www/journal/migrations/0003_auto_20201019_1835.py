# Generated by Django 3.1.2 on 2020-10-20 01:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_entry_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
