# Generated by Django 2.2.11 on 2020-07-27 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalog',
            old_name='category_id',
            new_name='category',
        ),
    ]
