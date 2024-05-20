import abc

from shared.core.domain import repository



class AccountRepository(repository.Repository):
    
    @abc.abstractmethod
    def find(self, name):
        pass