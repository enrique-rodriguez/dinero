import abc
from dataclasses import dataclass


@dataclass(frozen=True)
class ValueObject(abc.ABC):
    
    @abc.abstractmethod
    def get(self):
        pass

    def equals(self, other):
        return self.__eq__(other)
    
    def __eq__(self, other):
        other_value = other

        if not isinstance(other, str):
            other_value = other.get()
        
        return self.get() == other_value