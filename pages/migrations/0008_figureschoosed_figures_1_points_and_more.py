# Generated by Django 4.0.4 on 2022-05-14 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_remove_figureschoosed_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='figureschoosed',
            name='figures_1_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='figureschoosed',
            name='figures_2_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='figureschoosed',
            name='figures_3_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='figureschoosed',
            name='figures_4_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='figureschoosed',
            name='figures_5_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='figureschoosed',
            name='figures_6_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='figureschoosed',
            name='figures_7_points',
            field=models.IntegerField(default=0),
        ),
    ]
