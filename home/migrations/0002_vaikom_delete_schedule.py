# Generated by Django 4.2 on 2023-04-05 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaikom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=100)),
                ('departure', models.CharField(max_length=100)),
                ('arrival', models.CharField(max_length=100)),
                ('time_format', models.TimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
