from accounts import models
from django.shortcuts import render

from app import utils


def get_transactions(request):
    transactions = [
        {
            'account': m.account_id,
            'date': m.date,
            'payee': m.payee_id,
            'category': m.category_id,
            'memo': m.memo,
            'outflow': '' if m.outflow == 0 else utils.to_dollars(m.outflow),
            'inflow': '' if m.inflow == 0 else utils.to_dollars(m.inflow),
            'cleared': m.cleared,
        }
        for m in models.TransactionProjectionModel.objects.all()
    ]

    return render(request, 'app/accounts/transactions.html', {'transactions': transactions})