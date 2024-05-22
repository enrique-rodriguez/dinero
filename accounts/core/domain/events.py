from shared.core.domain import events


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

    def __init__(self, account_id, name, _type, balance, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.account_id = account_id
        self.name = name
        self._type = _type
        self.balance = balance
    
    def get_data(self):
        return {
            'account_id': self.account_id,
            'name': self.name,
            '_type': self._type,
            'balance': self.balance,
        }
    
    
    @classmethod
    def from_dict(cls, obj):
        return cls(
            id=obj.get('event_id'),
            created_at=obj.get('created_at'),
            account_id=obj.get('data').get('account_id'), 
            name=obj.get('data').get('name'),
            _type=obj.get('data').get('_type'), 
            balance=obj.get('data').get('balance'),
        )