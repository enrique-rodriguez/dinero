from accounts.core import factories
from accounts.core.domain import repository


class DjangoAccountRepository(repository.AccountRepository):

    def save(self, id, entity):
        from accounts import models

        for event in entity.domain_events:
            models.AccountEventModel.objects.create(
                event_id=event.id,
                account_id=id,
                created_at=event.created_at,
                event_name=event.__class__.__name__,
                data=event.get_data()
            )


    def get(self, account_id):
        from accounts import models

        evts = []

        for e in models.AccountEventModel.objects.filter(account_id=account_id):
            obj = e.data.copy()
            obj['event_id'] = e.event_id
            obj['created_at'] = e.created_at

            domain_event = factories.EventFactory.create(e.event_name, obj)
            
            if not domain_event:
                raise ValueError(f"Unhandled event '{e.event}'")
            
            evts.append(domain_event)

        return evts