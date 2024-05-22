import uuid

from django.db.utils import IntegrityError
from django.test import TestCase

from accounts import models


class TestAccountProjectModel(TestCase):

    def test_verbose_names(self):
        self.assertEqual(models.AccountProjectionModel._meta.verbose_name, 'Account Projection')
        self.assertEqual(models.AccountProjectionModel._meta.verbose_name_plural, 'Account Projections')

        self.assertEqual(models.AccountProjectionModel._meta.get_field('uuid').verbose_name, 'UUID')
        self.assertEqual(models.AccountProjectionModel._meta.get_field('name').verbose_name, 'Account Name')
        self.assertEqual(models.AccountProjectionModel._meta.get_field('category').verbose_name, 'Account Category')
        self.assertEqual(models.AccountProjectionModel._meta.get_field('type').verbose_name, 'Account Type')
        self.assertEqual(models.AccountProjectionModel._meta.get_field('balance').verbose_name, 'Account Balance')
    
    def test_field_names(self):
        self.assertEqual(models.AccountProjectionModel._meta.get_field('uuid').name, 'uuid')
        self.assertEqual(models.AccountProjectionModel._meta.get_field('name').name, 'name')
        self.assertEqual(models.AccountProjectionModel._meta.get_field('type').name, 'type')
        self.assertEqual(models.AccountProjectionModel._meta.get_field('category').name, 'category')
        self.assertEqual(models.AccountProjectionModel._meta.get_field('balance').name, 'balance')
    
    def test_uuid_is_unique(self):
        id = uuid.uuid4()

        models.AccountProjectionModel.objects.create(uuid=id, name='Account', balance=100)

        with self.assertRaises(IntegrityError):
            models.AccountProjectionModel.objects.create(uuid=id, name='Account', balance=100)



class TestAccountEventModel(TestCase):

    def test_verbose_names(self):
        self.assertEqual(models.AccountEventModel._meta.verbose_name, 'Account Event')
        self.assertEqual(models.AccountEventModel._meta.verbose_name_plural, 'Account Events')

        self.assertEqual(models.AccountEventModel._meta.get_field('event_id').verbose_name, 'Event ID')
        self.assertEqual(models.AccountEventModel._meta.get_field('created_at').verbose_name, 'Creation Datetime')
        self.assertEqual(models.AccountEventModel._meta.get_field('event_name').verbose_name, 'Event Name')
        self.assertEqual(models.AccountEventModel._meta.get_field('data').verbose_name, 'Event Data')
    
    def test_field_names(self):
        self.assertEqual(models.AccountEventModel._meta.get_field('event_id').name, 'event_id')
        self.assertEqual(models.AccountEventModel._meta.get_field('created_at').name, 'created_at')
        self.assertEqual(models.AccountEventModel._meta.get_field('event_name').name, 'event_name')
        self.assertEqual(models.AccountEventModel._meta.get_field('data').name, 'data')