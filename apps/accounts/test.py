from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelTests(TestCase):
    def test_create_user_with_default_role(self):
        User = get_user_model()

        user = User.objects.create_user(
            username="client_user",
            email="client@example.com",
            password="testpass123",
        )

        self.assertEqual(user.username, "client_user")
        self.assertEqual(user.role, User.Role.CLIENT)
        self.assertTrue(user.check_password("testpass123"))

    def test_create_owner_user(self):
        User = get_user_model()

        user = User.objects.create_user(
            username="owner_user",
            email="owner@example.com",
            password="testpass123",
            role=User.Role.OWNER,
        )

        self.assertEqual(user.role, User.Role.OWNER)
        self.assertTrue(user.check_password("testpass123"))