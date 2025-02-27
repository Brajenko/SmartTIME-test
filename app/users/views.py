from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from .serializers import UserSerializer


class RegisterView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class UserView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
