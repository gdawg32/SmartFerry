# Generated by Django 4.1.5 on 2023-04-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_irsensorvalue'),
    ]

    operations = [
        migrations.CreateModel(
            name='DHTSensorValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
            ],
        ),
    ]
