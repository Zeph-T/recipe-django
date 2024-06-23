from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser as User, Profile

class UrlsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345', email='test@example.com')  

    def tearDown(self):
        # Clean up created objects to avoid conflicts
        self.user.delete()

    def test_register_url(self):
        url = '/api/user/register/'
        response = self.client.post(url, {"email": "test3@test.com", "username": "testuser245", "password": "testpassword"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    
    def test_user_info_url(self):
        self.client.force_authenticate(user=self.user)
        url = '/api/user/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_profile_url(self):
        self.client.force_authenticate(user=self.user)
        url = '/api/user/profile/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_avatar_url(self):
        self.client.force_authenticate(user=self.user)
        url = '/api/user/profile/avatar/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_bookmark_url(self):
        self.client.force_authenticate(user=self.user)

        url = f'/api/user/profile/{self.user.pk}/bookmarks/'
        print(f'URL : {url}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_change_password_url(self):
        self.client.force_authenticate(user=self.user)
        url = '/api/user/password/change/'
        response = self.client.put(url , { "old_password": "12345", "new_password": "string1234"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    # def test_logout_url(self):
    #     self.client.force_authenticate(user=self.user)
    #     url = '/api/user/logout/'
    #     response = self.client.post(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)