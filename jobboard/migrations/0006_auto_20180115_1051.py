# Generated by Django 2.0 on 2018-01-15 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0005_vacancy_contract_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='contract_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
