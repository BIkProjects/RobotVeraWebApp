# Generated by Django 2.0.4 on 2018-07-30 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member_profile', '0001_initial'),
        ('jobboard', '0001_initial'),
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberOnVacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=66)),
                ('title', models.CharField(max_length=255)),
                ('experience', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('requirement', models.TextField(blank=True, null=True)),
                ('salary_from', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('salary_up_to', models.PositiveIntegerField(blank=True, null=True)),
                ('enabled', models.NullBooleanField(default=False)),
                ('published', models.BooleanField(default=False)),
                ('allowed_amount', models.CharField(max_length=127)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('busyness', models.ManyToManyField(blank=True, to='member_profile.Busyness')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='company.Company')),
                ('keywords', models.ManyToManyField(blank=True, to='jobboard.Keyword')),
                ('office', models.ManyToManyField(to='company.Office')),
                ('schedule', models.ManyToManyField(blank=True, to='member_profile.Schedule')),
                ('specialisations', models.ManyToManyField(blank=True, to='jobboard.Specialisation')),
            ],
            options={
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='VacancyOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.Vacancy')),
            ],
        ),
        migrations.AddField(
            model_name='memberonvacancy',
            name='vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.Vacancy'),
        ),
        migrations.AlterUniqueTogether(
            name='vacancyoffer',
            unique_together={('vacancy', 'member')},
        ),
        migrations.AlterUniqueTogether(
            name='memberonvacancy',
            unique_together={('member', 'vacancy')},
        ),
    ]
