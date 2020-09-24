from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance,filename):
    imagename , exception = filename.split(".")
    return "jops/%s.%s"%(instance.id,exception)


class Job(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    job_type = models.CharField(_("Job Type"), max_length=50 , choices=JOB_TYPE)
    description = models.TextField(_("Description"), max_length=1000)
    published_at = models.DateTimeField(_("Published At"), auto_now=True)
    vacancy = models.IntegerField(_("Vacancy"), default=1)
    salary = models.IntegerField(_("Salary"), default=0)
    experience = models.IntegerField(_("Experience"), default=0)
    category = models.ForeignKey('Category', verbose_name=_("Category"), on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(_("Image"), upload_to=image_upload )

    class Meta:
        verbose_name = _("Job")
        verbose_name_plural = _("Jobs")


    def __str__(self):
        return self.title




class Category(models.Model):
    name = models.CharField(_("Name"), max_length=30)
    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.name
