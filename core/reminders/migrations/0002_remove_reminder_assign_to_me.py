# Generated by Django 4.2.4 on 2023-10-25 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='assign_to_me',
        ),
    ]