# Generated by Django 2.0.3 on 2018-04-05 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0004_auto_20180405_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actiontype',
            name='condition_of_passage',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]