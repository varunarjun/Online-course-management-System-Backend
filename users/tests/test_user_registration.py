# users/tests/test_user_registration.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User

class UserRegistrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('register')  # This matches the path in users/urls.py
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'TestPassword123',
            'role': 'student'
        }

    def test_register_user(self):
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')
