# Generated by Django 2.0 on 2018-02-08 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0029_auto_20180206_0704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatevacancypassing',
            name='candidate',
        ),
        migrations.RemoveField(
            model_name='candidatevacancypassing',
            name='test',
        ),
        migrations.RemoveField(
            model_name='cvonvacancy',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='cvonvacancy',
            name='vacancy',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='employer',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='specializations',
        ),
        migrations.RemoveField(
            model_name='vacancytest',
            name='vacancy',
        ),
        migrations.DeleteModel(
            name='CandidateVacancyPassing',
        ),
        migrations.DeleteModel(
            name='CVOnVacancy',
        ),
        migrations.DeleteModel(
            name='Vacancy',
        ),
        migrations.DeleteModel(
            name='VacancyTest',
        ),
    ]
