from shared.core.domain import readmodel


class InMemoryReadModel(readmodel.ReadModelStore):
    
    def __init__(self):
        self.models = {}
    
    def get(self, id):
        return self.models.get(id)

    def save(self, id, model):
        self.models[id] = model
    
    def count(self):
        return len(self.models)