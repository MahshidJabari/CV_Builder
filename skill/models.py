from django.db import models
from lib.common_models import BaseModel


# Create your models here.

class Skill(BaseModel):
    cv = models.ForeignKey('resume.Resume', on_delete=models.CASCADE, related_name='cv_skill')


class Skills(BaseModel):
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=64, null=True)
    level = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Skill'
        ordering = ('created_time',)


class Language(BaseModel):
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE, related_name='languages')
    name = models.CharField(max_length=64, null=True)
    readingLevel = models.IntegerField(null=True)
    writingLevel = models.IntegerField(null=True)
    listeningLevel = models.IntegerField(null=True)
    speakingLevel = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Language'
        ordering = ('created_time',)


class AcademicCertificate(BaseModel):
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE, related_name='certifications')
    type = models.CharField(max_length=32, null=True)
    title = models.CharField(max_length=256, null=True)
    institute = models.CharField(max_length=256, null=True)
    year = models.CharField(max_length=16, null=True)
    month = models.CharField(max_length=16, null=True)

    class Meta:
        verbose_name = 'AcademicCertificate'
        ordering = ('created_time',)


class Honor(BaseModel):
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE, related_name='honors')
    title = models.CharField(max_length=256, null=True)
    year = models.CharField(max_length=16, null=True)
    month = models.CharField(max_length=16, null=True)

    class Meta:
        verbose_name = 'Honor'
        ordering = ('created_time',)
