# Generated by Django 3.2.9 on 2022-08-27 20:38

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_figures_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='figures',
            name='color',
        ),
        migrations.AddField(
            model_name='pointstext',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
    ]
