# Generated by Django 4.2.7 on 2023-12-07 08:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tasks", "0019_taskpriority_badge"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="participants",
            field=models.ManyToManyField(
                blank=True,
                related_name="tasks_participated",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
