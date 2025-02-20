from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Exam, Registration, Room
from .serializers import ExamSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ExamTests(APITestCase):
    def setUp(self):
        self.room = Room.objects.create(room_number=101)
        self.exam = Exam.objects.create(subject_name="Math", room=self.room)
        self.user = User.objects.create(email="testuser@example.com", password="testpassword123")
        self.second_user = User.objects.create(
            email="testuser2@example.com", password="testpassword123"
        )
        self.client.force_authenticate(user=self.user)  # type: ignore
        self.registration = Registration.objects.create(user=self.user, exam=self.exam)

    def test_list_exams(self):
        url = reverse("exams")
        response = self.client.get(url)
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_create_registration(self):
        url = reverse("create_registration")
        data = {"user": self.second_user.pk, "exam": self.exam.pk}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Registration.objects.count(), 2)
        self.assertEqual(
            Registration.objects.get(id=response.json()["id"]).user.id, self.second_user.pk
        )

    def test_delete_registration(self):
        url = reverse("delete_registration", kwargs={"pk": self.registration.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Registration.objects.count(), 0)

    def test_user_cannot_register_twice_for_same_exam(self):
        url = reverse("create_registration")
        data = {"user": self.user.pk, "exam": self.exam.pk}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Registration.objects.count(), 1)
