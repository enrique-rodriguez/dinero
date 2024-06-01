import uuid

from accounts.core.application import commands


from . import TestCase


class AddAccountTestCase(TestCase):

    def test_add_account_command_handler_is_registered(self):
        self.assertCommandRegistered(commands.AddAccountCommand)

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
    
    def test_raises_error_iftype_is_empty(self):
        result = self.add_account(account_type="")

        self.assertTrue(result.is_error)
        self.assertEqual(result.code, "account-creation-error")
        self.assertEqual(self.module.account_repository.count(), 0)

    def test_raises_error_if_balance_is_empty(self):
        result = self.add_account(account_balance="")

        self.assertTrue(result.is_error)
        self.assertEqual(result.code, "account-creation-error")
        self.assertEqual(self.module.account_repository.count(), 0)
    
    def test_account_added_to_read_model(self):
        self.add_account()

        self.assertEqual(self.module.account_read_model.count(), 1)