from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item (self):
        item = Menu.objects.create(Title = "Brocolli beef", Price = 16, Inventory =20)
        self.assertEqual(item.__str__(), "Brocolli beef : 16")