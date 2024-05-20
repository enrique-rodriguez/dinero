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


@dataclass(frozen=True)
class AccountName(values.ValueObject):
    name: str

    def __post_init__(self):
        if len(self.name) == 0:
            raise ValueError("Account Name Empty")
    
    def equals(self, other):
        return self == other
    
    def __eq__(self, other):
        if isinstance(other, str):
            other = AccountName(other)
        
        return other.name == self.name


class Account(entities.Entity):

    def __init__(self, events=None):
        super().__init__()
        
        evts = events or list()

        for e in evts: self.apply(e)
    
    def apply(self, event):
        if isinstance(event, events.AccountAddedEvent):
            self.apply_account_added_event(event)
        
        else:
            raise ValueError(f"Unknown event '{event.__class__.__name__}'")
    
    def apply_account_added_event(self, event: events.AccountAddedEvent):
        self.id = AccountId(event.id)
        self.name = AccountName(event.name)