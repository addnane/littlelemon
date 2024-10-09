#TestCase class
from django import test
from models import MenuTable

class MenuItemTest(test.TestCase):
 def test_get_item(self):
  item = MenuTable.objects.create(title="IceCream", price=80, inventory=100)
  self.assertEqual(item, "IceCream : 80")
