# Generated by Django 2.0 on 2018-02-01 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0018_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculumvitae',
            name='position',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cv.Position'),
        ),
    ]
