# Generated by Django 2.0.3 on 2018-04-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
