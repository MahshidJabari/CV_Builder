from rest_framework import serializers
from basicInfo.models import BasicInfo, Contact, SocialNetwork, BasicInfoList


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('email', 'mobile', 'phone', 'website', 'country', 'state',
                  'city', 'address')


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ('socialNetwork', 'profileID')


class BasicInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInfoList
        fields = ('firstName', 'lastName', 'resumeTitle', 'gender', 'maritalStatus', 'militaryService',
                  'birthDay', 'birthMonth', 'birthYear', 'resumeSummery', 'image',
                  'socialNetwork')


class BasicInfoSerializer(serializers.Serializer):
    language = serializers.CharField(max_length=16, write_only=True)
    is_active = serializers.BooleanField(write_only=True)
    basicInfo = BasicInfoListSerializer(many=False, write_only=True)
    contact = ContactSerializer(many=False, write_only=True)
    socialNetwork = SocialNetworkSerializer(many=True, required=True, write_only=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = BasicInfo
        fields = ('language', 'isActive', 'basicInfo', 'contact', 'socialNetwork')
