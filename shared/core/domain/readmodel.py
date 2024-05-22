import abc


class ReadModelStore(abc.ABC):

    @abc.abstractmethod
    def get(self, id):
        pass
    
    @abc.abstractmethod
    def save(self, id, model):
        pass