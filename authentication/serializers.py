from rest_framework import serializers
from authentication.models import User
from django.contrib.auth.hashers import make_password

from rest_framework.exceptions import *


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=False, write_only=True)
    password = serializers.CharField(max_length=256, write_only=True)
    token = serializers.CharField(read_only=True)

    def create(self, validated_data):
        try:
            user = User.objects.filter(email=validated_data['email']).first()
        except Exception:
            raise NotAuthenticated('Credential is wrong')
        if not user.check_password(validated_data['password']):
            raise AuthenticationFailed('authentication failed')
        else:
            token = user.get_tokens_for_user()
            return {'token': 'Bearer ' + token}

    class Meta:
        model = User
        fields = ('email', 'password', 'token')


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=False, write_only=True)
    password = serializers.CharField(max_length=256, write_only=True)

    def create(self, validated_data):
        try:
            user = User.objects.get(email=validated_data['email'])
            if user:
                raise ValidationError('user existed')
        except User.DoesNotExist:
            validated_data['password'] = make_password(validated_data['password'])
            return super().create(validated_data)

    class Meta:
        model = User
        fields = ('email', 'password')
