from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse

class MenuViewTesst(TestCase):

    def setup(self):
        item1 = Menu.objects.create(Title = "Brocolli beef", Price = 16, Inventory =20)
        item2 = Menu.objects.create(Title = "Chicken pepper", Price = 14, Inventory =22)

    def test_getall(self):
        url = reverse('menuitem')
        print(url)
        self.client.login(username = "admin",password = "lemon@789!")
        response= self.client.get(url)
        self.assertEqual(response.status_code, 200)


