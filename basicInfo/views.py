from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from resume.models import Resume
from rest_framework import status
from basicInfo.models import BasicInfo, Contact, SocialNetwork, BasicInfoList
from rest_framework.response import Response
from basicInfo.serializers import BasicInfoSerializer, ContactSerializer, BasicInfoListSerializer, \
    SocialNetworkSerializer


# Create your views here.
class BasicInfoView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = BasicInfoSerializer(data=request.data)
        if serializer.is_valid():
            language = serializer.validated_data.pop('language')
            is_active = serializer.validated_data.pop('isActive')
            cv = Resume.objects.create(language=language, owner_id=user.pk, isActive=is_active)
            basic_info = serializer.validated_data.pop('basicInfo')
            contact = serializer.validated_data.pop('contact')
            social_list = serializer.validated_data.pop('socialNetwork')
            info = BasicInfo.objects.create(cv_id=cv.pk)
            info_serializer = BasicInfoListSerializer(data=basic_info)
            contact_serializer = ContactSerializer(data=contact)
            social_serializer = SocialNetworkSerializer(data=social_list, many=True)

            if info_serializer.is_valid():
                BasicInfoList.objects.create(**info_serializer.validated_data, basic_id=info.pk)

            if contact_serializer.is_valid():
                Contact.objects.create(**contact_serializer.validated_data, basic_id=info.pk)

            if social_serializer.is_valid():
                SocialNetwork.objects.create(**social_serializer.validated_data, basic_id=info.pk)

        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
