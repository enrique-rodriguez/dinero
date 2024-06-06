import uuid

from accounts.core.application import commands


from . import TestCase


class AddAccountTestCase(TestCase):

    def add_payee(self, **kwargs):
        payee_id = kwargs.get('payee_id', str(uuid.uuid4()))
        payee_name = kwargs.get('payee_name', "Payee")
        
        return self.module.execute(commands.AddPayeeCommand(payee_id=payee_id, payee_name=payee_name))

    def test_add_account_command_handler_is_registered(self):
        self.assertCommandRegistered(commands.AddPayeeCommand)
    
    def test_creates_payee(self):
        payee_id = str(uuid.uuid4())

        result = self.add_payee(payee_id=payee_id)

        self.assertFalse(result.is_error)
        self.assertEqual(self.module.payee_repository.count(), 1)

    def test_payee_id_exists_gives_error(self):
        payee_id = str(uuid.uuid4())

        result = self.add_payee(payee_id=payee_id)
        result = self.add_payee(payee_id=payee_id)

        self.assertTrue(result.is_error)
        self.assertEqual(result.code, "payee-exists")
        self.assertEqual(self.module.payee_repository.count(), 1)
        
    def test_adds_the_payee(self):
        result = self.add_payee()

        self.assertFalse(result.is_error)
        self.assertEqual(self.module.payee_repository.count(), 1)
    
    def test_raises_error_if_payee_name_is_empty(self):
        result = self.add_payee(payee_name="")

        self.assertTrue(result.is_error)
        self.assertEqual(result.code, "payee-creation-error")
        self.assertEqual(self.module.payee_repository.count(), 0)