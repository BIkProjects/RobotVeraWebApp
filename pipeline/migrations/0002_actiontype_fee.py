# Generated by Django 2.0.3 on 2018-04-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actiontype',
            name='fee',
            field=models.BooleanField(default=False),
        ),
    ]
