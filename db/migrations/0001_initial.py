# Generated by Django 5.1.1 on 2024-10-05 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.SmallAutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=150, unique=True)),
                ("joined_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "user",
            },
        ),
        migrations.CreateModel(
            name="Menfess",
            fields=[
                (
                    "tweet_id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="menfesses",
                        to="db.user",
                    ),
                ),
            ],
            options={
                "db_table": "menfess",
            },
        ),
    ]
