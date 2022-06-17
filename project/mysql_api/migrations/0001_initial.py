# Generated by Django 4.0.5 on 2022-06-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='current_weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateField()),
                ('temp', models.FloatField()),
                ('main', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=25)),
                ('icon', models.CharField(max_length=25)),
            ],
        ),
    ]