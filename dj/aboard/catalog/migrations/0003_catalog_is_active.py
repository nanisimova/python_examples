# Generated by Django 2.2.11 on 2020-07-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200727_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
