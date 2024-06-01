import uuid
import unittest

from tests.accounts.core import module

from accounts.core.application import commands


class TestCase(unittest.TestCase):
    def setUp(self):
        self.module = module.get_module()

    def assertCommandRegistered(self, command):
        self.assertTrue(self.module.is_command_registered(command))

    def add_account(self, **kwargs):
        account_id = kwargs.get("account_id", str(uuid.uuid4()))
        account_name = kwargs.get("account_name", "My Account")
        account_type = kwargs.get("account_type", "checking")
        account_balance = kwargs.get("account_balance", "100.00")

        cmd = commands.AddAccountCommand(account_id, account_name, account_type, account_balance)

        return self.module.execute(cmd)