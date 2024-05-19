import uuid

from django.test import TestCase
from django.db.utils import IntegrityError
from accounts import models


class TestAccountModel(TestCase):

    def test_verbose_names(self):
        self.assertEqual(models.AccountModel._meta.verbose_name, 'Account')
        self.assertEqual(models.AccountModel._meta.verbose_name_plural, 'Accounts')

        self.assertEqual(models.AccountModel._meta.get_field('uuid').verbose_name, 'UUID')
        self.assertEqual(models.AccountModel._meta.get_field('name').verbose_name, 'name')
    
    def test_field_names(self):
        self.assertEqual(models.AccountModel._meta.get_field('uuid').name, 'uuid')
        self.assertEqual(models.AccountModel._meta.get_field('name').name, 'name')
    
    def test_uuid_is_unique(self):
        id = uuid.uuid4()

        models.AccountModel.objects.create(uuid=id, name='Account')

        with self.assertRaises(IntegrityError):
            models.AccountModel.objects.create(uuid=id, name='Account')
