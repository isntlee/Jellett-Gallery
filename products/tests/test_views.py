from django.test import TestCase

from products.models import Product, Category


class TestProductViews(TestCase):

    def setUp(self):
        category = Category(name='maria_sharia')
        category.save()
        valid_product = Product(name='name', description='description', offer='99.00')
        valid_product.save()

    def test_query_returns_results(self):
        response = self.client.get('/?query=anything')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'includes/main-nav.html')

    def test_empty_query_returns_artists_page(self):
        response = self.client.get('/?query=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'includes/main-nav.html')
        self.assertTrue(response, 'home/artists.html')

    def test_render_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'includes/main-nav.html')
        self.assertTrue(response, 'home/index.html')

    # def test_render_product_detail(self):
    #     valid_product = Product.objects.get(id=4)
    #     response = self.client.get(f'/products/{id}/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'products/product_detail.html')
    #     self.assertTrue(response.context['product'])

