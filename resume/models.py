from django.db import models

from lib.common_models import BaseModel


# Create your models here.
class Resume(BaseModel):
    language = models.CharField(max_length=8, null=False)
    owner = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='user')
    isActive = models.BooleanField(null=True)

    class Meta:
        verbose_name = 'Resume'
        ordering = ('created_time', 'isActive')
