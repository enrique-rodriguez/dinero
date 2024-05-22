

class AccountReadModel:

    def __init__(self, account_id=None, name=None, category=None, type=None, balance=None):
        self.account_id = account_id
        self.name = name
        self.category = category
        self.type = type
        self.balance = balance