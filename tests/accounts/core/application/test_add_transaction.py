import uuid

from . import TestCase

from accounts.core.application import commands


class AddTransactionTestCase(TestCase):

    def setUp(self):
        super().setUp()

        self.account_id = str(uuid.uuid4())
        self.payee_id = str(uuid.uuid4())
        self.category_id = str(uuid.uuid4())
        
        # We must first add an account before we can add any transactions to it.
        self.add_account(account_id=self.account_id)
        # TODO: Create a payee
        # TODO: Create a category
    
    def add_transaction(self, **kwargs):
        account_id = kwargs.get("account_id")
        transaction_id = kwargs.get("transaction_id")
        date = kwargs.get("date", "20240312")
        payee_id = kwargs.get("payee_id", self.payee_id)
        memo = kwargs.get("memo", "Memo")
        category_id = kwargs.get("category_id", self.category_id)

        cmd = commands.AddTransactionCommand(transaction_id, account_id, date, payee_id, category_id, memo)

        return self.module.execute(cmd)
    
    def test_add_transaction_command_handler_is_registered(self):
        self.assertCommandRegistered(commands.AddTransactionCommand)
    
    def test_account_not_found_results_in_an_error(self):    
        transaction_id = str(uuid.uuid4())
        
        result = self.add_transaction(transaction_id=transaction_id, account_id=str(uuid.uuid4()) )

        self.assertTrue(result.is_error)
        self.assertEqual(result.code, 'account-not-found')

    def test_transaction_with_id_already_exists_results_in_an_error(self):
        transaction_id = str(uuid.uuid4())

        result = self.add_transaction(transaction_id=transaction_id, account_id=self.account_id)
        result = self.add_transaction(transaction_id=transaction_id, account_id=self.account_id)

        self.assertTrue(result.is_error)
        self.assertEqual(result.code, "transaction-creation-error")
    
    def test_transaction_with_no_date_gives_error(self):
        transaction_id = str(uuid.uuid4())
        
        result = self.add_transaction(transaction_id=transaction_id, account_id=self.account_id, date='')

        self.assertTrue(result.is_error)
        self.assertEqual(result.code, "transaction-creation-error")
    
    def test_transaction_with_no_payee_gives_error(self):
        transaction_id = str(uuid.uuid4())
        
        result = self.add_transaction(transaction_id=transaction_id, account_id=self.account_id, payee_id='')

        self.assertTrue(result.is_error)
        self.assertEqual(result.code, "transaction-creation-error")
    
    def test_transaction_with_no_memo_is_valid(self):
        transaction_id = str(uuid.uuid4())
        
        result = self.add_transaction(transaction_id=transaction_id, account_id=self.account_id, memo='')

        self.assertFalse(result.is_error)
    
    def test_transaction_with_no_category_id_gives_error(self):
        transaction_id = str(uuid.uuid4())
        
        result = self.add_transaction(transaction_id=transaction_id, account_id=self.account_id, category_id='')

        self.assertTrue(result.is_error)
        self.assertEqual(result.code, "transaction-creation-error")
    
    # # TODO: Implement test case
    # def test_invalid_payee_id_gives_error(self):
    #     account_id = str(uuid.uuid4())
    #     transaction_id = str(uuid.uuid4())
        
    #     # We must first add an account before we can add any transactions to it.
    #     self.add_account(account_id=account_id)

    #     result = self.add_transaction(transaction_id=transaction_id, account_id=account_id, category_id='')

    #     self.assertTrue(result.is_error)
    #     self.assertEqual(result.code, 'payee-not-found')
    
    # # TODO: Implement test case
    # def test_invalid_category_id_gives_error(self):
    #     account_id = str(uuid.uuid4())
    #     transaction_id = str(uuid.uuid4())
        
    #     # We must first add an account before we can add any transactions to it.
    #     self.add_account(account_id=account_id)

    #     result = self.add_transaction(transaction_id=transaction_id, account_id=account_id, category_id='')

    #     self.assertTrue(result.is_error)
    #     self.assertEqual(result.code, 'category-not-found')
