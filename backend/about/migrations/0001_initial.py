# Generated by Django 4.1.7 on 2023-07-25 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Montag', 'montag'), ('Dienstag', 'dienstag'), ('Mittwoch', 'mittwoch'), ('Donnerstag', 'donnerstag'), ('Freitag', 'freitag'), ('Samstag', 'samstag'), ('Sonntag', 'sonntag')], max_length=50)),
                ('time_morning_from', models.TimeField(null=True)),
                ('time_morning_to', models.TimeField(null=True)),
                ('time_afternoon_from', models.TimeField(null=True)),
                ('time_afternoon_to', models.TimeField(null=True)),
            ],
        ),
    ]
