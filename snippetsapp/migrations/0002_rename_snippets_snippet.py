# Generated by Django 4.1.5 on 2023-02-05 08:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("snippetsapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Snippets",
            new_name="Snippet",
        ),
    ]
