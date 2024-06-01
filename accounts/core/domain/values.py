from dataclasses import dataclass

from shared.core.domain import values


@dataclass(frozen=True)
class TransactionId(values.ValueObject):
    id: str

    def get(self):
        return self.id


@dataclass(frozen=True)
class PayeeId(values.ValueObject):
    id: str

    def __post_init__(self):
        if len(self.id) == 0:
            raise ValueError("Transaction Payee Empty.")

    def get(self):
        return self.id


@dataclass(frozen=True)
class CategoryId(values.ValueObject):
    id: str

    def __post_init__(self):
        if len(self.id) == 0:
            raise ValueError("Category Empty.")

    def get(self):
        return self.id

@dataclass(frozen=True)
class TransactionMemo(values.ValueObject):
    memo: str

    # def __post_init__(self):
    #     if len(self.id) == 0:
    #         raise ValueError("Transaction Payee Empty.")

    def get(self):
        return self.memo
    

@dataclass(frozen=True)
class TransactionDate(values.ValueObject):
    date: str

    def __post_init__(self):
        if self.date == '':
            raise ValueError("Transaction Date Empty.")

    def get(self):
        return self.date


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



@dataclass(frozen=True)
class AccountCategory(values.ValueObject):
    category: str

    def __post_init__(self):
        if len(self.category) == 0:
            raise ValueError("Account Category Empty")
    
    def get(self):
        return self.category

    @classmethod
    def from_type(self, type):
        if type.get() in ["checking", "savings", "cash"]:
            return AccountCategory("budget")

        elif type.get() in ["asset", "liability"]:
            return AccountCategory("tracking")
        
        raise ValueError(f"Unknown category mapping to assign for account type '{type}'")