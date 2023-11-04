# Generated by Django 4.2.6 on 2023-11-03 20:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Mail",
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
                ("sender", models.EmailField(max_length=254)),
                ("recipient", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=255)),
                ("body", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("is_read", models.BooleanField(default=False)),
                ("is_archived", models.BooleanField(default=False)),
                ("is_deleted", models.BooleanField(default=False)),
                ("is_starred", models.BooleanField(default=False)),
                ("cc", models.EmailField(blank=True, max_length=254, null=True)),
                ("bcc", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "attachments",
                    models.FileField(blank=True, null=True, upload_to="attachments"),
                ),
                (
                    "importance",
                    models.CharField(
                        choices=[
                            ("HIGH", "HIGH"),
                            ("MEDIUM", "MEDIUM"),
                            ("LOW", "LOW"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "folder",
                    models.CharField(
                        choices=[
                            ("INBOX", "INBOX"),
                            ("SENT", "SENT"),
                            ("DRAFT", "DRAFT"),
                        ],
                        max_length=20,
                    ),
                ),
                ("is_draft", models.BooleanField(default=False)),
                ("reply_to", models.EmailField(blank=True, max_length=254, null=True)),
                ("thread_it", models.CharField(blank=True, max_length=255, null=True)),
                ("is_replied", models.BooleanField(default=False)),
                ("is_forwarded", models.BooleanField(default=False)),
                ("tags", models.ManyToManyField(to="mail.tag")),
            ],
        ),
    ]