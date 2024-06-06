from accounts.core.domain import values
from shared.core.domain import entities


class Payee(entities.Entity):
    def __init__(self, id, name, *args, **kwargs):
        super(*args, **kwargs)
        self.id = id
        self.name = name

    def apply(self, event):
        pass


