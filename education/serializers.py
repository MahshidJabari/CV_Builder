from rest_framework import serializers
from education.models import Education, Work


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('educationLevel', 'fieldOfStudy', 'branch', 'instituteTitle', 'gpa', 'country',
                  'state', 'city', 'entrance', 'graduateYear', 'currentlyStudying', 'cv_id')


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('position', 'categoryTitle', 'employerType', 'company', 'employmentType', 'level', 'country',
                  'state', 'city', 'startYear', 'startMonth', 'finishYear', 'finishMonth', 'present', 'task', 'cv_id')
