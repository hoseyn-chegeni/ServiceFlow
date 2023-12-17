# Generated by Django 4.2.8 on 2023-12-17 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("flow", "0006_alter_workflow_diagram"),
        ("tasks", "0030_alter_tasklogflow_flow_alter_tasklogflow_state"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="current_state",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="flow.state",
            ),
        ),
    ]
