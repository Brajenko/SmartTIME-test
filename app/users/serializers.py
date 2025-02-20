from rest_framework import serializers

from .models import User
from app.exams.serializers import RegistrationNoUserSerializer


class UserSerializer(serializers.ModelSerializer):
    registrations = RegistrationNoUserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        exclude = ["exams"]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ["is_admin", "last_login"]

    def create(self, validated_data):
        return User.objects.create(
            email=validated_data["email"],
            password=validated_data["password"],
        )
