from rest_framework import serializers
from project.models import Project, Projects, Research


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', "company", "linkUrl", "year", "month", "description")


class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = ('publishType', "title", "publisher", "linkUrl", "year", "month", "description")


class ProjectSerializer(serializers.ModelSerializer):
    projects = ProjectListSerializer(many=True)
    research = ResearchSerializer(many=True)

    class Meta:
        model = Project
        fields = ('cv_id', "projects", "research")
