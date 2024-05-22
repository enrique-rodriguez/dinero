import uuid
from django.test import TestCase

from accounts.core.domain import models
from accounts.core.infrastructure import readmodel


class DjangoAccountReadModelTestCase(TestCase):

    def setUp(self):
        self.store = readmodel.DjangoAccountReadModelStore()

    def test_model_not_found_gives_none(self):
        self.assertIsNone(self.store.get(str(uuid.uuid4())))
    
    def test_saves_model(self):
        account_id = str(uuid.uuid4())
        name = 'name'
        type = 'type'
        balance = 200
        
        model = models.AccountReadModel(
            account_id,
            name,
            type,
            balance
        )

        self.store.save(account_id, model)

        fetched_model = self.store.get(account_id)

        self.assertEqual(fetched_model.account_id, account_id)
        self.assertEqual(fetched_model.name, name)
        self.assertEqual(fetched_model.type, type)
        self.assertEqual(fetched_model.balance, balance)
    
    def test_updates_model(self):
        account_id = str(uuid.uuid4())
        name = 'name'
        type = 'type'
        balance = 200
        
        model = models.AccountReadModel(
            account_id,
            name,
            type,
            balance
        )

        self.store.save(account_id, model)

        model.name = "new name"

        self.store.save(account_id, model)

        fetched_model = self.store.get(account_id)

        self.assertEqual(fetched_model.name, "new name")
    
    def test_only_updates_if_save_is_called(self):
        account_id = str(uuid.uuid4())
        name = 'name'
        type = 'type'
        balance = 200
        
        model = models.AccountReadModel(
            account_id,
            name,
            type,
            balance
        )

        self.store.save(account_id, model)

        model.name = "new name"

        fetched_model = self.store.get(account_id)

        self.assertEqual(fetched_model.name, "name")
