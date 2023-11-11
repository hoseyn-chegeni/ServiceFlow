# Generated by Django 4.2.6 on 2023-11-11 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DatabaseLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("event_type", models.CharField(max_length=255)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("table_name", models.CharField(max_length=255)),
                ("record_id", models.PositiveIntegerField()),
                ("field_name", models.CharField(max_length=255)),
                ("additional_info", models.TextField(blank=True, null=True)),
                ("is_success", models.BooleanField(default=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]