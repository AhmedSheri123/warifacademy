# Generated by Django 4.1.1 on 2022-10-01 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_alter_figuresinfo_figures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='figuresinfo',
            name='figures',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.figures', verbose_name='السمة'),
        ),
    ]
