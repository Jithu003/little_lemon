from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from restaurant.models import Menu
from decimal import Decimal


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Pizza", price=9.99, inventory=10)
        self.assertEqual(item, "Pizza : 9.99")



    




        



