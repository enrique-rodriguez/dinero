from accounts.core import factories
from accounts.core.domain import repository


class DjangoAccountRepository(repository.AccountRepository):

    def save(self, id, entity):
        from accounts import models

        account_id = id

        if not isinstance(id, str):
            account_id = id.get()

        for event in entity.domain_events:
            models.AccountEventModel.objects.create(
                event_id=event.id,
                account_id=account_id,
                created_at=event.created_at,
                event_name=event.__class__.__name__,
                data=event.get_data()
            )


    def get(self, account_id):
        from accounts import models

        id = account_id

        if not isinstance(account_id, str):
            id = account_id.get()

        evts = []

        for e in models.AccountEventModel.objects.filter(account_id=id):
            obj = {}
            obj['event_id'] = e.event_id
            obj['created_at'] = e.created_at
            obj['data'] = e.data.copy()

            domain_event = factories.EventFactory.create(e.event_name, obj)
            
            if not domain_event:
                raise ValueError(f"Unhandled event '{e.event}'")
            
            evts.append(domain_event)

        return evts