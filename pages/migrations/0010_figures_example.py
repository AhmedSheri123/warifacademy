# Generated by Django 3.2.9 on 2022-08-27 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_pointstext'),
    ]

    operations = [
        migrations.AddField(
            model_name='figures',
            name='_example',
            field=models.TextField(blank=True, null=True, verbose_name='مثال'),
        ),
    ]
