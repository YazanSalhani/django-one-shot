# Generated by Django 5.0.6 on 2024-05-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TodoList",
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
                ("string", models.CharField(max_length=100)),
                ("date_time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
