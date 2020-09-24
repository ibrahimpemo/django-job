from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

class Job(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    job_type = models.CharField(_("Job Type"), max_length=50 , choices=JOB_TYPE)
    description = models.TextField(_("Description"), max_length=1000)
    published_at = models.DateTimeField(_("Published At"), auto_now=True)
    vacancy = models.IntegerField(_("Vacancy"), default=1)
    salary = models.IntegerField(_("Salary"), default=0)
    experience = models.IntegerField(_("Experience"), default=0)

    def __str__(self):
        return self.title