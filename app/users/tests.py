from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


class UserTests(APITestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.user_data = {"email": "testuser@example.com", "password": "testpassword123"}
        self.user = self.user_model.objects.create(**self.user_data)

    def test_register_user(self):
        url = reverse("register")
        data = {"email": "newuser@example.com", "password": "newpassword123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.user_model.objects.count(), 2)
        self.assertEqual(self.user_model.objects.get(email=data["email"]).email, data["email"])

    def test_list_users(self):
        url = reverse("users", args=[self.user.pk])
        self.client.force_authenticate(user=self.user)  # type: ignore
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["email"], self.user.email)

    def test_list_users_unauthenticated(self):
        url = reverse("users", args=[self.user.pk])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json()["detail"], "Authentication credentials were not provided.")
