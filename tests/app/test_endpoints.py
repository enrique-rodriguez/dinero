from django.test import TestCase
from django.urls import reverse


class AccountsEndpointTestCase(TestCase):

    def test_response(self):
        url = reverse('accounts')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/accounts/index.html')