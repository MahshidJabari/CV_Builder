from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from project.serializers import ProjectSerializer, ProjectListSerializer, ResearchSerializer
from project.models import Project, Projects, Research


# Create your views here.
class ProjectView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            cv_id = serializer.validated_data.pop('cv_id')
            try:
                project = Project.objects.create(cv_id=cv_id)
            except Exception:
                return Response(status=status.HTTP_403_FORBIDDEN)
            project_list = serializer.validated_data.pop('projects')
            research_list = serializer.validated_data.pop('research')
            projects_serializer = ProjectListSerializer(data=project_list, many=True)
            if projects_serializer.is_valid():
                Projects.objects.create(**projects_serializer.validated_data, skill=project.pk)

            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

            research_serializer = ResearchSerializer(data=research_list, many=True)
            if research_serializer.is_valid():
                Research.objects.create(**research_serializer.validated_data, skill=project.pk)

            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
