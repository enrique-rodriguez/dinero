from accounts.core.domain import events
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
            data = e.data
            event_id = e.event_id

            if e.event == events.AccountAddedEvent.__name__:
            
                domain_event = events.AccountAddedEvent.create(
                    id=event_id,
                    account_id=account_id, 
                    created_at=e.created_at,
                    data=data
                )
            
            else:
                raise ValueError(f"Unhandled event '{e.event}'")
            
            evts.append(domain_event)

        return evts