# Generated by Django 4.1.7 on 2023-05-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0003_alter_data_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=14),
        ),
    ]