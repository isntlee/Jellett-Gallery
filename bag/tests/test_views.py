from django.test import TestCase
from products.models import Product
from django.contrib.auth.models import User


class TestCartViews(TestCase):

    def test_get_add_product_to_bag(self):
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

    def test_get_delete_item_from_bag(self):
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
        page = self.client.get("/bag/")

        session = self.client.session
        session["bag"] = "bag_session"

        quantity = 1
        response = self.client.post("/bag/",
                                    kwargs={"product_id": product.id},
                                    data={"quantity": quantity},
                                    follow=True)

        page = self.client.get("/bag/")
        self.assertEqual(page.status_code, 200)

        delete_item = self.client.post("/bag/",
                                       kwargs={"product_id": product.id},
                                       data={"quantity": (quantity - 1)},
                                       follow=True)

        page = self.client.get("/bag/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bag/bag.html")
