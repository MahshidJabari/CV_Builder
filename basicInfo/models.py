from django.db import models
from lib.common_models import BaseModel


# Create your models here.
class BasicInfo(BaseModel):
    cv = models.ForeignKey('resume.Resume', on_delete=models.CASCADE, related_name='infos')


class BasicInfoList(BaseModel):
    basic = models.ForeignKey('BasicInfo', on_delete=models.CASCADE, related_name="basics")
    firstName = models.CharField(max_length=64, null=False)
    lastName = models.CharField(max_length=64, null=False)
    resumeTitle = models.CharField(max_length=64, null=False)
    gender = models.CharField(max_length=8, null=True)
    maritalStatus = models.CharField(max_length=8, null=True)
    militaryService = models.CharField(max_length=32, null=True)
    birthDay = models.CharField(max_length=16, null=True)
    birthMonth = models.CharField(max_length=16, null=True)
    birthYear = models.CharField(max_length=16, null=True)
    resumeSummery = models.CharField(max_length=2048, null=True)
    image = models.CharField(max_length=8192, null=True)

    class Meta:
        ordering = ('created_time',)
        verbose_name = 'BasicInfoList'

    def __str__(self):
        return self.firstName


class Contact(BaseModel):
    basic = models.ForeignKey('BasicInfo', on_delete=models.CASCADE, related_name="contacts")
    email = models.EmailField(max_length=256, null=False)
    mobile = models.CharField(max_length=15, null=False)
    phone = models.CharField(max_length=15, null=True)
    website = models.URLField(null=True)
    country = models.CharField(max_length=64, null=True)
    state = models.CharField(max_length=64, null=True)
    city = models.CharField(max_length=64, null=True)
    address = models.CharField(max_length=64, null=True)

    class Meta:
        ordering = ('created_time',)
        verbose_name = 'Contact'

    def __str__(self):
        return self.email


class SocialNetwork(BaseModel):
    basic = models.ForeignKey('BasicInfo', on_delete=models.CASCADE, related_name="socialNetworks")
    socialNetwork = models.CharField(max_length=16, null=True)
    profileID = models.CharField(max_length=64, null=True)

    class Meta:
        ordering = ('created_time',)
        verbose_name = 'SocialNetwork'

    def __str__(self):
        return self.profileID
