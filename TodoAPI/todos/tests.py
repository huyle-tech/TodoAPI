from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Todo

from django.contrib.auth.models import User


class TodoTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)

    def test_create_todo(self):
        url = '/api/todos/'
        data = {
            'title': 'Meeting',
            'description': 'at 9 am',
            'completed': False
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

    def test_list_todo(self):
        url = '/api/todos/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_todo(self):
        todo = Todo.objects.create(title='Old Meeting', description='at 9am yesterday', completed=False)
        url = '/api/todos/{}/'.format(todo.id)
        data = {
            'title': 'Updated Meeting',
            'description': 'at 9 am today',
            'completed': True
        }
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])

    def test_delete_todo(self):
        todo = Todo.objects.create(title='Test Todo', description='Test description', completed=False)
        url = '/api/todos/{}/'.format(todo.id)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 0)

    def test_unauthorized_access(self):
        # Do NOT send token
        self.client.credentials()
        url = '/api/todos/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


