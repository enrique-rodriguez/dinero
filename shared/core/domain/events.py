import abc
import uuid
from datetime import datetime


class DomainEvent(abc.ABC):
    def __init__(self, id=None, created_at=None):
        self.id = id or str(uuid.uuid4())
        self.created_at = created_at or datetime.now()

    @abc.abstractmethod
    def get_data(self):
        pass