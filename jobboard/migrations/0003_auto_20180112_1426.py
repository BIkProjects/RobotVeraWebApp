# Generated by Django 2.0 on 2018-01-12 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0002_auto_20180112_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='email',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='phone',
        ),
    ]
