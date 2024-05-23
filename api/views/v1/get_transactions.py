from django.shortcuts import render


def get_transactions(request):
    return render(request, 'app/accounts/transactions.html')