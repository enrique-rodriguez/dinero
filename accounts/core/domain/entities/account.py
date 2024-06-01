from accounts.core.domain import events
from accounts.core.domain import values
from accounts.core.application import commands
from shared.core.domain import entities


class Transaction(entities.Entity):
    def __init__(self, id, date, payee_id, category_id, memo, *args, **kwargs):
        super(*args, **kwargs)
        self.id = id
        self.date = date
        self.payee_id = payee_id
        self.category_id = category_id
        self.memo = memo

    def apply(self, event):
        pass


class Account(entities.Entity):

    def __init__(self, events=None):
        super().__init__()
        self.transactions = []
        
        for e in (events or list()): self.apply(e)
    
    def add_transaction(self, cmd: commands.AddTransactionCommand):
        payee_id = values.PayeeId(cmd.payee_id)
        memo = values.TransactionMemo(cmd.memo)
        category_id = values.CategoryId(cmd.category_id)
        transaction_date = values.TransactionDate(cmd.date)
        transaction_id = values.TransactionId(cmd.transaction_id)

        if self.get_transaction(transaction_id):
            raise ValueError(f"Transaction with id '{transaction_id.get()}' already exists.")
        
        self.add_event(events.TransactionAddedEvent(
            transaction_id=transaction_id, 
            account_id=self.id,
            date=transaction_date,
            payee_id=payee_id,
            category_id=category_id,
            memo=memo,
        ))

    def get_transaction(self, id):
        for t in self.transactions:
            if t.id == id:
                return t
        return None
    
    def apply(self, event):
        if isinstance(event, events.AccountAddedEvent):
            return self.apply_account_added_event(event)
        
        if isinstance(event, events.TransactionAddedEvent):
            return self.apply_transaction_added_event(event)
        
        raise ValueError(f"Unknown event '{event.__class__.__name__}'")

    def apply_account_added_event(self, event: events.AccountAddedEvent):
        self.name = event.name
        self.type = event.type
        self.id = event.account_id
        self.balance = event.balance
        self.category = event.category

    def apply_transaction_added_event(self, event: events.TransactionAddedEvent):
        self.transactions.append(Transaction(
            id=event.transaction_id,
            date=event.date,
            payee_id=event.payee_id,
            category_id=event.category_id,
            memo=event.memo,
        ))