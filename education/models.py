from django.db import models
from lib.common_models import BaseModel


# Create your models here.

class Education(BaseModel):
    cv = models.ForeignKey('resume.Resume', on_delete=models.CASCADE, related_name='cv')
    educationLevel = models.CharField(max_length=64, null=True)
    fieldOfStudy = models.CharField(max_length=64, null=True)
    branch = models.CharField(max_length=128, null=True)
    instituteTitle = models.CharField(max_length=128, null=True)
    gpa = models.CharField(max_length=128, null=True)
    country = models.CharField(max_length=64, null=True)
    state = models.CharField(max_length=64, null=True)
    city = models.CharField(max_length=128, null=True)
    entrance = models.CharField(max_length=8, null=True)
    graduateYear = models.CharField(max_length=8, null=True)
    currentlyStudying = models.BooleanField(null=True)

    class Meta:
        verbose_name = 'Education'
        ordering = ('created_time',)


class Work(BaseModel):
    cv = models.ForeignKey('resume.Resume', on_delete=models.CASCADE, related_name='works_cv')
    position = models.CharField(max_length=64, null=True)
    categoryTitle = models.CharField(max_length=32, null=True)
    employerType = models.CharField(max_length=64, null=True)
    company = models.CharField(max_length=128, null=True)
    employmentType = models.CharField(max_length=64, null=True)
    level = models.CharField(max_length=64, null=True)
    country = models.CharField(max_length=64, null=True)
    state = models.CharField(max_length=64, null=True)
    city = models.CharField(max_length=128, null=True)
    startYear = models.CharField(max_length=16, null=True)
    startMonth = models.CharField(max_length=16, null=True)
    finishYear = models.CharField(max_length=16, null=True)
    finishMonth = models.CharField(max_length=16, null=True)
    present = models.BooleanField(null=True)
    task = models.CharField(max_length=2048, null=True)

    class Meta:
        ordering = ('created_time',)
