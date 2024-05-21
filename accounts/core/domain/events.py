from shared.core.domain import events


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
    def create(cls, event_id, account_id, created_at, data):
        return cls(
            id=event_id,
            account_id=account_id, 
            created_at=created_at,
            name=data.get('name'),
            _type=data.get('_type'), 
            balance=data.get('balance'),
        )