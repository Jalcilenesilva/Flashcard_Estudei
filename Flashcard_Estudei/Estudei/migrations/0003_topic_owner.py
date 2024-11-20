# Generated by Django 5.1.1 on 2024-09-15 15:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Estudei", "0002_entry"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="topic",
            name="owner",
            field=models.ForeignKey(
                default=3,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
