from django.http import HttpResponse

from accounts import models

from app import utils


def get_balance(request):
    category = request.GET.get("cat", "budget")

    if category not in ["budget",  "tracking"]:
        return HttpResponse(status=400)
    
    balance = sum([a.balance for a in models.AccountProjectionModel.objects.filter(category=category)])
        
    return HttpResponse(utils.to_dollars(balance))