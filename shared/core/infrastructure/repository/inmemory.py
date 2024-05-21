from shared.core.domain import repository


class InMemoryRepository(repository.Repository):

    def __init__(self):
        self.entities = dict()

    def get(self, id):
        entity = self.entities.get(id)

        return [] if not entity else entity.domain_events

    def save(self, id, entity):
        self.entities[id] = entity