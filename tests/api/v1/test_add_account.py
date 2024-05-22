from django import urls
from django.test import TestCase


class AddAccountApiEndpointTestCase(TestCase):

    def setUp(self):
        self.url = urls.reverse("api:add_account")

    def add_account(self, **kwargs):

        data = {
            'account_name': kwargs.get('account_name', 'My Account'),
            'account_type': kwargs.get('account_type', 'Savings'),
            'account_balance': kwargs.get('account_balance', '100.00'),
        }

        return self.client.post(self.url, data)

    def test_successful_account_creation_redirects_to_home(self):
        response = self.add_account()
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers.get("HX-Redirect"), urls.reverse("home"))
    
    # def test_account_with_name_already_exists_gives_400(self):
    #     response = self.add_account()
        
    #     self.assertEqual(response.status_code, 400)

    def test_gives_405_on_GET(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 405)
    
    def test_bad_request_if_account_name_not_given(self):
        response = self.add_account(account_name='')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'Could not create account: Account Name Empty')
    
    def test_bad_request_if_account_type_not_given(self):
        response = self.add_account(account_type='')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'Could not create account: Account Type Empty')
    
    def test_bad_request_if_account_type_not_given(self):
        response = self.add_account(account_balance='')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'Could not create account: Account Balance Empty')
    
    