from django.test import TestCase


class CheckoutViewsTests(TestCase):

    def test_get_checkout_response_not_logged_in(self):
        response = self.client.get("/checkout/")
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")