from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_creste_user_with_email_successfull(self):
        '''test crerting a new user if email succesfull'''
        email="test@test.com"
        password="123456789"
        user = get_user_model().objects.create_user(
            
            email='test@test.com', password='123456789'
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalizer(self):
        '''Testb the email for new user is normalized'''
        email = 'test@test.com'
        user = get_user_model().objects.create_user(
            email,'test123'
        )
        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')

    def test_create_new_superuser(self):
        '''test creating a new superuser'''
        user=get_user_model().objects.create_superuser(
            'test@test.com',
            '123456789'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    