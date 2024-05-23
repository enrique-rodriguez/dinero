import uuid

from django import urls
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import View

from accounts import accounts
from accounts.core.application import commands


class AddAccountEndpoint(View):

    def post(self, request):
        account_id = str(uuid.uuid4())
        account_name = request.POST.get("account_name", "")
        account_type = request.POST.get("account_type", "")
        account_balance = request.POST.get("account_balance", "")

        status, content = self.add_account(account_id, account_name, account_type, account_balance)

        return HttpResponse(content, status=status, headers={'HX-Redirect': urls.reverse("home")})

    def add_account(self, account_id, account_name, account_type, account_balance):
        status = 201
        message_type = "success"
        message = f"Account created successfully."

        cmd = commands.AddAccountCommand(account_id, account_name, account_type, account_balance)

        try:
            result = accounts.execute(cmd)

            if result.is_error:
                status = 400
                message = result.msg
                message_type = "warning"
            
        except Exception as error:
            print(error)
            message = "Unexpected Error"
            status = 500
            message_type = "error"

        getattr(messages, message_type)(self.request, message)

        return status, message
        

add_account = AddAccountEndpoint.as_view()