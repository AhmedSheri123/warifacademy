# Generated by Django 4.1.1 on 2022-10-01 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_figuresinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='figuresinfo',
            name='figures',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.figures', unique=True, verbose_name='السمة'),
        ),
    ]