from django import urls
from django.test import TestCase


class GetTransactionsApiEndpointTestCase(TestCase):

    def setUp(self):
        self.url = urls.reverse("api:get-transactions")

    def get_transactions(self, **kwargs):

        return self.client.get(self.url)

    
    def test_response(self):
        response = self.get_transactions()

        self.assertEqual(response.status_code, 200)
    