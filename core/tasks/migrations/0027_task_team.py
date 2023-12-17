# Generated by Django 4.2.8 on 2023-12-16 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("team", "0011_remove_team_team"),
        ("tasks", "0026_remove_tasklogflow_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="team.team",
            ),
        ),
    ]