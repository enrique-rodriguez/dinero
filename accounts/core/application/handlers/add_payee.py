from accounts.core import factories
from accounts.core.domain import events
from accounts.core.domain import entities
from accounts.core.domain import values
from accounts.core.domain import repository
from accounts.core.application import commands

from shared.core.application import handlers, result


class AddPayeeHandler(handlers.CommandHandler):

    def __init__(self, payee_repository: repository.PayeeRepository):
        super().__init__()
        self.payee_repository = payee_repository

    def execute(self, cmd: commands.AddPayeeCommand):

        res = result.Result.success()

        if self.payee_repository.get(cmd.payee_id):
            return result.Result.error(f"Payee with id '{cmd.payee_id}' already exists", "payee-exists")

        try:
            payee = entities.Payee(values.PayeeId(cmd.payee_id), values.PayeeName(cmd.payee_name))
            self.payee_repository.save(cmd.payee_id, payee)
        except ValueError as e:
            res = result.Result.error(str(e), "payee-creation-error")


        return res



