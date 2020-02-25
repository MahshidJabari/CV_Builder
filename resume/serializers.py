from rest_framework import serializers
from resume.models import Resume
from education.serializers import EducationSerializer, WorkSerializer
from basicInfo.serializers import BasicInfoSerializer


class ResumeSerializer(serializers.ModelSerializer):
    basicInfo = BasicInfoSerializer(many=False)
    educations = EducationSerializer(many=True)
    works = WorkSerializer(many=True)

    class Meta:
        model = Resume
        fields = ('language',)
