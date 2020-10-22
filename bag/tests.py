from django.test import TestCase
from products.models import Product
from django.contrib.auth.models import User
# from django.urls import reverse


class TestCartViews(TestCase):

    def test_add_product_to_cart(self):
        User.objects.create_user(
            email='testUser@example.com',
            username='testUser',
            password='passw0rd')
        self.client.login(username='testUser', password='passw0rd')
        product = Product.objects.create(name='Test Product',
                                         description='Some content',
                                         offer='99.00')

        self.assertEqual(Product.objects.count(), 1)
        response = self.client.get("/products/1/".format(Product.pk))

        session = self.client.session
        session['bag'] = 'bag_session'

        response = self.client.post("/bag/",
                                    kwargs={'product_id': product.id})
        page = self.client.get("/bag/")
        self.assertEqual(page.status_code, 200)
