from shared.core.domain import events
from accounts.core.domain import values


class AccountUpdatedEvent(events.DomainEvent):
    def __init__(self, account_id, name, category, type, balance, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.account_id = account_id
        self.name = name
        self.category = category
        self.type = type
        self.balance = balance
    
    def get_data(self):
        return {
            'account_id': self.account_id,
            'name': self.name,
            'category': self.category,
            'type': self.type,
            'balance': self.balance,
        }


class AccountAddedEvent(events.DomainEvent):

    def __init__(self, account_id, name, type, category, balance, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.account_id = account_id
        self.name = name
        self.type = type
        self.category = category
        self.balance = balance
    
    def get_data(self):
        return {
            'account_id': self.account_id.get(),
            'name': self.name.get(),
            'type': self.type.get(),
            'category': self.category.get(),
            'balance': self.balance.get(),
        }
    
    
    @classmethod
    def from_dict(cls, obj):
        return cls(
            id=obj.get('event_id'),
            created_at=obj.get('created_at'),
            account_id=values.AccountId(obj.get('data').get('account_id')), 
            name=values.AccountName(obj.get('data').get('name')),
            type=values.AccountType(obj.get('data').get('type')), 
            category=values.AccountCategory(obj.get('data').get('category')),
            balance=values.AccountBalance(obj.get('data').get('balance')),
        )


class TransactionAddedEvent(events.DomainEvent):

    def __init__(self, transaction_id, account_id, date, payee_id, category_id, memo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.account_id = account_id
        self.transaction_id = transaction_id
        self.date = date
        self.payee_id = payee_id
        self.category_id = category_id
        self.memo = memo
    
    def get_data(self):
        return {
            'account_id': self.account_id.get(),
            'transaction_id': self.transaction_id.get(),
            'date': self.date.get(),
            'payee_id': self.payee_id.get(),
            'category_id': self.category_id.get(),
            'memo': self.memo.get(),
        }
    
    @classmethod
    def from_dict(cls, obj):
        return cls(
            id=obj.get('event_id'),
            created_at=obj.get('created_at'),
            account_id=values.AccountId(obj.get('data').get('account_id')), 
            transaction_id=values.TransactionId(obj.get('data').get('transaction_id')),
            date=values.TransactionDate(obj.get('data').get('date')), 
            payee_id=values.PayeeId(obj.get('data').get('payee_id')), 
            category_id=values.CategoryId(obj.get('data').get('category_id')), 
            memo=values.TransactionMemo(obj.get('data').get('memo')), 
        )