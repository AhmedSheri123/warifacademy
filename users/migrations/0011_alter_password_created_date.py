# Generated by Django 4.1.1 on 2022-10-01 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_password_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 1, 17, 13, 27, 436465)),
        ),
    ]
