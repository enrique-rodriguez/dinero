import abc


class Repository(abc.ABC):

    @abc.abstractmethod
    def save(self, id, entity):
        pass

    @abc.abstractmethod
    def get(self, id):
        pass