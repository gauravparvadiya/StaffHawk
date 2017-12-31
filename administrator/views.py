from django.shortcuts import render, redirect
from .models import FreelanceAccount
from Authentication.models import User
from bde.models import Contract


def index(request):
    if request.session.has_key('username'):
        return render(request, "administrator/dashboard.html")
    else:
        return redirect("/")


def redirect_to_add_freelance_account(request):
    if request.session.has_key('username'):
        return render(request, "administrator/add_freelance_account.html")
    else:
        return redirect("/")


def upwork_account(request):
    if request.session.has_key('username'):
        all_upwork_account = FreelanceAccount.objects.filter(account_type='1')
        if all_upwork_account.count() > 0:
            return render(request, "administrator/upwork_accounts.html", {'upwork_accounts': all_upwork_account})
        else:
            return render(request, "administrator/upwork_accounts.html")
    else:
        return redirect("/")


def guru_account(request):
    if request.session.has_key('username'):
        all_guru_account = FreelanceAccount.objects.filter(account_type='2')
        if all_guru_account.count() > 0:
            return render(request, "administrator/guru_accounts.html", {'guru_accounts': all_guru_account})
        else:
            return render(request, "administrator/guru_accounts.html")
    else:
        return redirect("/")


def admin_account(request):
    if request.session.has_key('username'):
        all_admin_account = User.objects.filter(user_role='1')
        if all_admin_account.count() > 0:
            return render(request, "administrator/admin_accounts.html", {'admin_accounts': all_admin_account})
        else:
            return render(request, "administrator/admin_accounts.html")
    else:
        return redirect("/")


def bde_account(request):
    if request.session.has_key('username'):
        all_bde_account = User.objects.filter(user_role='2')
        if all_bde_account.count() > 0:
            return render(request, "administrator/bde_accounts.html", {'bde_accounts': all_bde_account})
        else:
            return render(request, "administrator/bde_accounts.html")
    else:
        return redirect("/")


def tl_account(request):
    if request.session.has_key('username'):
        all_tl_account = User.objects.filter(user_role='3')
        if all_tl_account.count() > 0:
            return render(request, "administrator/tl_accounts.html", {'tl_accounts': all_tl_account})
        else:
            return render(request, "administrator/tl_accounts.html")
    else:
        return redirect("/")


def employee_account(request):
    if request.session.has_key('username'):
        all_employee_account = User.objects.filter(user_role='4')
        if all_employee_account.count() > 0:
            return render(request, "administrator/employee_accounts.html", {'employee_accounts': all_employee_account})
        else:
            return render(request, "administrator/employee_accounts.html")
    else:
        return redirect("/")


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect("/")


def applied_jobs(request):
    jobs_list = Contract.objects.all()
    return render(request,"administrator/applied_jobs.html",{'jobs_lists': jobs_list})