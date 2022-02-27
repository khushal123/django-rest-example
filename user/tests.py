from django.urls import reverse
from user.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class UserTests(APITestCase):
    def test_get(self):
        url = reverse('user-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = reverse('user-view')
        data = {
            "first_name": "test",
            "last_name": "test",
            "company_name": "test",
            "city": "Brighton",
            "state": "MI",
            "zip": 48116,
            "email": "test@gmail.com",
            "web": "http://www.chanayjeffreyaesq.com",
            "age": 48
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().first_name, 'test')

    def test_get_by_id(self):
        try:
            user_id = User.objects.order_by('id').last().id 
        except:
            user_id = 2
        url = reverse("user-details", kwargs={"id": user_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        try:
            user_id = User.objects.order_by('id').last().id 
        except:
            user_id = 2
        url = reverse("user-details", kwargs={"id": user_id})
        data = {
            "first_name": "updated_test",
            "last_name": "test",
        }
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete(self):
        try:
            user_id = User.objects.order_by('id').last().id 
        except:
            user_id = 3
        url = reverse("user-details", kwargs={"id": user_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
