from rest_framework import serializers

from .models import Exam, Registration


class ExamSerializer(serializers.ModelSerializer):
    room = serializers.IntegerField(source="room.room_number")

    class Meta:
        model = Exam
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"


class RegistrationNoUserSerializer(serializers.ModelSerializer):
    exam = ExamSerializer()

    class Meta:
        model = Registration
        exclude = ["user"]
