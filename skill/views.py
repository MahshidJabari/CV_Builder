from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from skill.serializers import SkillSerializer, SkillsSerializer, LanguageSerializer, HonorSerializer, \
    CertificateSerializer
from skill.models import Skill, Language, Honor, AcademicCertificate, Skills


# Create your views here.
class SkillView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SkillSerializer

    def create(self, request, *args, **kwargs):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            cv_id = serializer.validated_data.pop('cv_id')
            try:
                skill = Skill.objects.create(cv_id=cv_id)
            except Exception:
                return Response(status=status.HTTP_403_FORBIDDEN)
            language_list = serializer.validated_data.pop('language')
            skill_list = serializer.validated_data.pop('skills')
            honor_list = serializer.validated_data.pop('honor')
            certificate_list = serializer.validated_data.pop('certificate')

            language_serializer = LanguageSerializer(data=language_list, many=True)
            if language_serializer.is_valid():
                Language.objects.create(**language_serializer.validated_data, skill=skill.pk)

            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

            skills_serializer = SkillsSerializer(data=skill_list, many=True)
            if skills_serializer.is_valid():
                Skills.objects.create(**skills_serializer.validated_data, skill=skill.pk)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

            honor_serializer = HonorSerializer(data=honor_list, many=True)
            if honor_serializer.is_valid():
                Honor.objects.create(**honor_serializer.validated_data, skill=skill.pk)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

            certificate_serializer = CertificateSerializer(data=certificate_list, many=True)
            if honor_serializer.is_valid():
                AcademicCertificate.objects.create(**certificate_serializer.validated_data, skill=skill.pk)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
