# Generated by Django 4.1.7 on 2023-07-25 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opening',
            name='time_afternoon_from',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opening',
            name='time_afternoon_to',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opening',
            name='time_morning_from',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opening',
            name='time_morning_to',
            field=models.TimeField(blank=True, null=True),
        ),
    ]