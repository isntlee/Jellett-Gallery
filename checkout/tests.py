from django.test import TestCase
import uuid

# Create your tests here.

from django.test import TestCase
from .models import Order, OrderLineItem

# Create your tests here.

class TestOrder(TestCase):
    """ Testing the Order model """
    def test_order(self):

        order_number = uuid.uuid4().hex.upper()

        string = Order(id = "1", date = "2020-03-20 18:06:34.021189+00:00", full_name="Test_name")
        self.assertEqual(str(string), "1-2020-03-20 18:06:34.021189+00:00-Test_name")