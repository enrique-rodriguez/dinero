from dataclasses import dataclass

from accounts.core.domain import events
from shared.core.domain import entities
from shared.core.domain import values


@dataclass(frozen=True)
class AccountId(values.ValueObject):
    id: str

    def __post_init__(self):
        if len(self.id) == 0:
            raise ValueError("Account ID Empty")

    def get(self):
        return self.id


@dataclass(frozen=True)
class AccountBalance(values.ValueObject):
    balance: str

    def __post_init__(self):
        if len(str(self.balance)) == 0:
            raise ValueError("Account Balance Empty")
    
    def get(self):
        return self.balance
            
    def clean(self):
        new_balance = None

        try:
            new_balance = float(self.balance.strip())

        except:
            new_balance = float('0')
        
        return AccountBalance(int(new_balance * 100))
        

@dataclass(frozen=True)
class AccountType(values.ValueObject):
    type: str

    def __post_init__(self):
        if len(self.type) == 0:
            raise ValueError("Account Type Empty")
    
    def get(self):
        return self.type
        

@dataclass(frozen=True)
class AccountName(values.ValueObject):
    name: str

    def __post_init__(self):
        if len(self.name) == 0:
            raise ValueError("Account Name Empty")
    
    def get(self):
        return self.name



class Account(entities.Entity):

    def __init__(self, events=None):
        super().__init__()
        
        evts = events or list()

        for e in evts: self.apply(e)
    
    def apply(self, event):
        if isinstance(event, events.AccountAddedEvent):
            return self.apply_account_added_event(event)
        
        raise ValueError(f"Unknown event '{event.__class__.__name__}'")

    def apply_account_added_event(self, event: events.AccountAddedEvent):
        self.id = AccountId(event.account_id)
        self.name = AccountName(event.name)
        self.type = AccountType(event._type)
        self.balance = AccountBalance(event.balance).clean()