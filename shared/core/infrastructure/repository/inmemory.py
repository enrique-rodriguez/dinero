from shared.core.domain import repository


class InMemoryRepository(repository.Repository):

    def __init__(self):
        self.entities = dict()

    def get(self, id):
        return self.entities.get(id)

    def save(self, id, entity):
        self.entities[id] = entity