from django.test import TestCase


class BagUrlsTests(TestCase):

    def test_view_bag_template(self):
        response = self.client.get('/bag/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
