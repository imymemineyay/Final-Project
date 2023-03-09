# Generated by Django 4.1.1 on 2023-02-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                ("complete", models.BooleanField(default=False)),
                ("create", models.DateField(auto_now_add=True)),
            ],
            options={"ordering": ["create"],},
        ),
        migrations.DeleteModel(name="Todo",),
    ]
