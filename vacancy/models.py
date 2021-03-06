from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse

from jobboard.handlers.oracle import OracleHandler
from member_profile.models import Busyness, Schedule
from users.models import Member


class Vacancy(models.Model):
    company = models.ForeignKey('company.Company',
                                blank=False,
                                null=False,
                                on_delete=models.CASCADE,
                                related_name='vacancies')
    uuid = models.CharField(max_length=66,
                            blank=False,
                            null=False)
    created_by = models.ForeignKey('users.Member',
                                   on_delete=models.SET_NULL,
                                   null=True)

    title = models.CharField(max_length=255)
    specialisations = models.ManyToManyField('jobboard.Specialisation',
                                             blank=True)
    keywords = models.ManyToManyField('jobboard.Keyword',
                                      blank=True)
    experience = models.CharField(max_length=10,
                                  null=True,
                                  blank=True)
    description = models.TextField(blank=True,
                                   null=True)
    requirement = models.TextField(blank=True,
                                   null=True)
    office = models.ManyToManyField('company.Office')
    salary_from = models.PositiveIntegerField(default=0,
                                              blank=True,
                                              null=True)
    salary_up_to = models.PositiveIntegerField(blank=True,
                                               null=True)
    busyness = models.ManyToManyField(Busyness,
                                      blank=True)
    schedule = models.ManyToManyField(Schedule,
                                      blank=True)
    enabled = models.NullBooleanField(default=False)
    published = models.BooleanField(default=False)
    allowed_amount = models.CharField(max_length=127)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_statistic_url(self):
        return reverse('vacancystatistic', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('vacancy', kwargs={'pk': self.id})

    def __str__(self):
        return '{}: {}'.format(self.company.name, self.title)

    @property
    def candidates(self):
        """
        Filter for members subscribed to vacancy
        :return: Members QuerySet
        """
        members = OracleHandler().get_members_on_vacancy(self.company.contract_address, self.uuid)
        return get_user_model().objects.filter(contract_address__in=[i['contract_address'] for i in members])

    @property
    def chain_allowed_amount(self):
        return OracleHandler().vacancy(self.company.contract_address, self.uuid)['allowed_amount'] / 10 ** 18

    @property
    def chain(self):
        return OracleHandler().vacancy(self.company.contract_address, self.uuid)

    @property
    def user_field_name(self):
        return 'company.collaborators'

    class Meta:
        ordering = ('-updated_at',)


class MemberOnVacancy(models.Model):
    member = models.ForeignKey(Member,
                               on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy,
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('member', 'vacancy'),)


class VacancyOffer(models.Model):
    vacancy = models.ForeignKey('vacancy.Vacancy',
                                on_delete=models.CASCADE)
    member = models.ForeignKey(Member,
                               on_delete=models.CASCADE,
                               related_name='offers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True,
                                   blank=True,
                                   default='')

    class Meta:
        unique_together = (("vacancy", "member"),)

    def __str__(self):
        return 'Vacancy offer'

    def refuse(self, description=None):
        self.is_active = False
        self.description = description
        self.save()
