from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient,APITestCase

class MenuViewTesst(TestCase):

    def setUp(self):
        item1 = Menu.objects.create(Title = "Brocolli beef", Price = 16, Inventory =20)
        item2 = Menu.objects.create(Title = "Chicken pepper", Price = 14, Inventory =22)
        self.user = User.objects.create_user(username="testuser2", password="testpassword")
        # generate token
        self.token, created = Token.objects.get_or_create(user=self.user)
        print(f'token: {self.token.key}')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION = "Token" + self.token.key)

    def test_getall(self):
        url = reverse('home')
        print(url)
        response= self.client.get(url)
        self.assertEqual(response.status_code, 200)


