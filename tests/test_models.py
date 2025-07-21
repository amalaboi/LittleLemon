from django.test import TestCase
# add models from restaurant
from restaurant.models import Menu

# Create your tests here.

class MenuTest(TestCase):
    
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        # print('item => ',str(item))
        self.assertEqual(str(item), 'IceCream : 80')
    