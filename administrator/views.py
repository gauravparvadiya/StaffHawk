from django.shortcuts import render
from .models import FreelanceAccount

def index(request):
    return render(request, "administrator/dashboard.html")


def redirect_to_add_freelance_account(request):
    return render(request, "administrator/add_freelance_account.html")


def upwork_account(request):
    all_upwork_account = FreelanceAccount.objects.filter(account_type='1')
    if all_upwork_account.count() > 0:
        return render(request, "administrator/upwork_accounts.html",{'upwork_accounts':all_upwork_account})
    else:
        return render(request, "administrator/upwork_accounts.html")


def guru_account(request):
    all_guru_account = FreelanceAccount.objects.filter(account_type='2')
    if all_guru_account.count() > 0:
        return render(request, "administrator/guru_accounts.html",{'guru_accounts':all_guru_account})
    else:
        return render(request, "administrator/guru_accounts.html")