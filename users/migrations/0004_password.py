# Generated by Django 3.2.9 on 2022-05-15 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_users_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=250)),
                ('is_enabled', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2022, 5, 16, 0, 8, 11, 477646))),
            ],
        ),
    ]