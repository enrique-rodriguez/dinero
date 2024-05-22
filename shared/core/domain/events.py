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

    def to_dict(self):
        return {
            'event_id': self.id,
            'created_at': self.created_at,
            'event_name': self.__class__.__name__,
            'data': self.get_data()
        }