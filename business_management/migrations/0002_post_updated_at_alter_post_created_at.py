# Generated by Django 4.1.1 on 2023-02-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("business_management", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
