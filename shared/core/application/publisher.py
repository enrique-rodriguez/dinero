import abc


class MessagePublisher(abc.ABC):

    @abc.abstractmethod
    def publish(self, message):
        pass