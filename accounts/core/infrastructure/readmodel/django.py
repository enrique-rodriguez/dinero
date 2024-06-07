from accounts.core.domain.models import AccountReadModel
from shared.core.domain import readmodel


class DjangoAccountReadModelStore(readmodel.ReadModelStore):
    
    def __init__(self):
        self.m = None

    def get(self, id):
        projection = self.get_model_by_id(id)
        
        if not projection:
            return None
        
        return AccountReadModel(
            str(projection.uuid),
            projection.name,
            projection.category,
            projection.type,
            projection.balance,
        )
    
    def save(self, id, model):
        from accounts.models import AccountProjectionModel

        projection = self.get_model_by_id(id)
        
        if not projection:
            projection = AccountProjectionModel()
        
        projection.uuid = model.account_id
        projection.name = model.name
        projection.category = model.category
        projection.type = model.type
        projection.balance = model.balance

        projection.save()
    
    def get_model_by_id(self, id):
        from accounts.models import AccountProjectionModel

        try:
            model = AccountProjectionModel.objects.get(uuid=id)
        except AccountProjectionModel.DoesNotExist:
            model = None
        
        return model
    

class DjangoTransactionsReadModelStore(readmodel.ReadModelStore):
    def get(self, id):
        pass
    
    def save(self, id, model):
        pass