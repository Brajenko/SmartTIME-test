from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView

from .models import Exam, Registration
from .serializers import ExamSerializer, RegistrationSerializer


class ListExams(ListAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()


class CreateRegistration(CreateAPIView):
    serializer_class = RegistrationSerializer
    queryset = Registration.objects.all()


class DeleteRegistration(DestroyAPIView):
    serializer_class = RegistrationSerializer
    queryset = Registration.objects.all()
