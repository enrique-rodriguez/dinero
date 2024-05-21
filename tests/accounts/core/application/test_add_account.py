import uuid
import unittest

from accounts.core.application import commands

from tests.accounts.core import module


class AddAccountTestCase(unittest.TestCase):

    def setUp(self):
        self.module = module.create_module()
    
    def add_account(self, **kwargs):
        account_id = kwargs.get("account_id", str(uuid.uuid4()))
        account_name = kwargs.get("account_name", "My Account")
        account_type = kwargs.get("account_type", "Savings")
        account_balance = kwargs.get("account_balance", "100.00")

        cmd = commands.AddAccountCommand(account_id, account_name, account_type, account_balance)

        return self.module.execute(cmd)
    
    def test_add_account_command_handler_is_registered(self):
        self.assertTrue(self.module.is_command_registered(commands.AddAccountCommand))

    def test_account_id_exists_gives_error(self):
        account_id = str(uuid.uuid4())

        result = self.add_account(account_id=account_id)
        result = self.add_account(account_id=account_id)

        self.assertTrue(result.is_error)
        self.assertEqual(result.code, "account-exists")
        self.assertEqual(self.module.account_repository.count(), 1)
        
    def test_adds_the_account(self):
        result = self.add_account()

        self.assertFalse(result.is_error)
        self.assertEqual(self.module.account_repository.count(), 1)
    
    def test_raises_error_if_account_name_is_empty(self):
        result = self.add_account(account_name="")

        self.assertTrue(result.is_error)
        self.assertEqual(result.code, "account-creation-error")
        self.assertEqual(self.module.account_repository.count(), 0)

    def test_raises_error_if_account_id_is_empty(self):
        result = self.add_account(account_id="")

        self.assertTrue(result.is_error)
        self.assertEqual(result.code, "account-creation-error")
        self.assertEqual(self.module.account_repository.count(), 0)
    
    def test_raises_error_if_type_is_empty(self):
        result = self.add_account(account_type="")

        self.assertTrue(result.is_error)
        self.assertEqual(result.code, "account-creation-error")
        self.assertEqual(self.module.account_repository.count(), 0)

    def test_raises_error_if_balance_is_empty(self):
        result = self.add_account(account_balance="")

        self.assertTrue(result.is_error)
        self.assertEqual(result.code, "account-creation-error")
        self.assertEqual(self.module.account_repository.count(), 0)