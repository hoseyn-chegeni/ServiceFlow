# Generated by Django 4.2.7 on 2023-12-07 09:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("department", "0004_rename_org_department_dept"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="department",
            name="dept",
        ),
    ]