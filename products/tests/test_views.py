from django.test import TestCase

from products.models import Product, Category


class TestProductViews(TestCase):

    def setUp(self):
        category = Category(name='maria_sharia')
        category.save()
        product = Product(name='name', description='description', offer='99.00')
        product.save()

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

    def test_render_product_detail(self):
        product = Product.objects.get()
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertTrue(response.context['product'])

    def test_render_category(self):
        category = Category.objects.get()
        response = self.client.get(f'/products/?category={category.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_render_404_not_found(self):
        response = self.client.get('/product/0/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed('404.html')
