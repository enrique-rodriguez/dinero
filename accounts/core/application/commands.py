from dataclasses import dataclass

from shared.core.application import messages


@dataclass(frozen=True)
class AddAccountCommand(messages.Command):
    id: str
    name: str
    type: str
    balance: str


@dataclass(frozen=True)
class AddTransactionCommand(messages.Command):
    transaction_id: str
    account_id: str
    date: str
    payee_id: str
    category_id: str
    memo: str