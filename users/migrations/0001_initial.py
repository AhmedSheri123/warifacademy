# Generated by Django 4.0.4 on 2022-05-11 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='اسم المستخدم')),
                ('email', models.EmailField(max_length=254, verbose_name='ايميل')),
            ],
        ),
    ]
