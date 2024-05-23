from django.shortcuts import render
from django.http import HttpResponse

from accounts import models

from app import utils


def get_accounts_view_model(accounts):
    return [
        {
            'name': acct.name,
            'balance': utils.to_dollars(acct.balance),
            'debt': True if acct.balance < 0 else False
        }
        
        for acct in accounts
    ]


def get_accounts(request):
    category = request.GET.get("cat", "budget")

    if category not in ["budget",  "tracking"]:
        return HttpResponse(status=400)
    
    accounts = get_accounts_view_model(models.AccountProjectionModel.objects.filter(category=category))

    return render(request, 'app/layout/sidebar/accounts.html', {'accounts': accounts})