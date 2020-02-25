from rest_framework.generics import *
from rest_framework.permissions import AllowAny
from authentication.serializers import UserLoginSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication


# Create your views here.


class LoginView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer


class SignUpView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
