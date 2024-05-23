from django import urls
from django.test import TestCase


class GetBalanceApiEndpointTestCase(TestCase):

    def setUp(self):
        self.url = urls.reverse("api:get-balance")

    def get_balance(self, **kwargs):

        data = {'cat': kwargs.get('cat', 'budget')}

        return self.client.get(self.url, data)

    
    def test_bad_request_if_not_budget_or_tracking(self):
        response = self.get_balance(cat='invalid_category')

        self.assertEqual(response.status_code, 400)
    
    def test_budget_category_balance(self):
        response = self.get_balance(cat='budget')

        self.assertEqual(response.status_code, 200)    
        self.assertEqual(response.content, b'$0.00')    
    
    def test_tracking_category_balance(self):
        response = self.get_balance(cat='tracking')

        self.assertEqual(response.status_code, 200)   
        self.assertEqual(response.content, b'$0.00') 