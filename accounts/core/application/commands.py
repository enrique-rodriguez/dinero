from dataclasses import dataclass
from shared.core.application import messages


@dataclass(frozen=True)
class AddAccountCommand(messages.Command):
    id: str
    name: str