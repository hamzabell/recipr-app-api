from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email(self):
        """Test creating a user with a new user with email is successfully"""
        email = "test@mailinator.com"
        password = "Test123"
        user = get_user_model().objects.create_user(
            email = email,
            password= password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for the new user is normalized"""
        email = "test@MAILINATOR.COM"
        user = get_user_model().objects.create_user(
            email,
            'test123'
        )

        self.assertEqual(user.email, email.lower())

    def test_user_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            "test@mailinator.com",
            "test123"
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)