from dataclasses import dataclass
from shared.core.domain import events


@dataclass(frozen=True)
class AccountAddedEvent(events.DomainEvent):
    id: str
    name: str