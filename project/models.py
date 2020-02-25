from django.db import models
from lib.common_models import BaseModel


# Create your models here.

class Project(BaseModel):
    cv = models.ForeignKey('resume.Resume', on_delete=models.CASCADE, related_name='cv_project')


class Projects(BaseModel):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=256, null=True)
    company = models.CharField(max_length=256, null=True)
    linkUrl = models.URLField(null=True)
    year = models.CharField(max_length=16, null=True)
    month = models.CharField(max_length=16, null=True)
    description = models.CharField(max_length=4096, null=True)

    class Meta:
        verbose_name = 'Project'
        ordering = ('created_time',)


class Research(BaseModel):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='researches')
    publishType = models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=256, null=True)
    publisher = models.CharField(max_length=64, null=True)
    linkUrl = models.URLField(null=True)
    year = models.CharField(max_length=16, null=True)
    month = models.CharField(max_length=16, null=True)
    description = models.CharField(max_length=4096, null=True)

    class Meta:
        verbose_name = 'Research'
        ordering = ('created_time',)
