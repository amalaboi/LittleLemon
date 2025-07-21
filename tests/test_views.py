from django.test import TestCase
# add models from restaurant
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Eba",price=5.00,inventory=40)
        Menu.objects.create(title="Suya",price=13.99,inventory=60)
    
    def test_getall(self):
        eba = Menu.objects.get(title="Eba")
        suya = Menu.objects.get(title="Suya")
        self.assertEqual(str(eba),'Eba : 5.00')
        self.assertEqual(str(suya),'Suya : 13.99')
        
        
