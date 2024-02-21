# store/tests/test_cart.py

from django.test import TestCase
from django.urls import reverse
from store.models import Product

class CartTestCase(TestCase):
    def setUp(self):
        # Set up any necessary test data, such as creating products
        self.product = Product.objects.create(title='Test Product', price=10.00)

    def test_cart_add(self):
        # Test adding an item to the cart
        response = self.client.post(reverse('cart:cart_add'), {'productid': self.product.id, 'productqty': 1, 'action': 'post'})
        self.assertEqual(response.status_code, 200)

        # You can add more assertions here to verify the behavior of adding to the cart

    # Add more test methods as needed to cover different functionalities of the cart

    def test_cart_delete(self):
        # Test deleting an item from the cart
        response = self.client.post(reverse('cart:cart_delete'), {'productid': self.product.id, 'action': 'post'})
        self.assertEqual(response.status_code, 200)

        # You can add more assertions here to verify the behavior of deleting from the cart
