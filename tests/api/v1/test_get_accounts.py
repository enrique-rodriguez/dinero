from django import urls
from django.test import TestCase


class GetAccountsApiEndpointTestCase(TestCase):

    def setUp(self):
        self.url = urls.reverse("api:get-accounts")

    def get_accounts(self, **kwargs):

        data = {'cat': kwargs.get('cat', 'budget')}

        return self.client.get(self.url, data)

    def test_template_used(self):
        response = self.get_accounts(cat='budget')

        self.assertTemplateUsed(response, 'app/layout/sidebar/accounts.html')
    
    def test_account_list_in_context(self):
        response = self.get_accounts(cat='budget')

        self.assertIn('accounts', response.context)

    
    def test_bad_request_if_not_budget_or_tracking(self):
        response = self.get_accounts(cat='invalid_category')

        self.assertEqual(response.status_code, 400)
    
    def test_budget_category_accounts(self):
        response = self.get_accounts(cat='budget')

        self.assertEqual(response.status_code, 200)    
    
    def test_tracking_category_accounts(self):
        response = self.get_accounts(cat='tracking')

        self.assertEqual(response.status_code, 200)   
