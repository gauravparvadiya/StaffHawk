from django.shortcuts import render
from .models import ProjectSize
from administrator.models import FreelanceAccount


def index(request):
    if request.session.has_key('username'):
        return render(request, "bde/dashboard.html")
    else:
        return render(request, "Authentication/login.html")


def add_application(request):
    project_size = ProjectSize.objects.all()
    freelance_account = FreelanceAccount.objects.all()
    return render(request, "bde/add_application.html",{'project_sizes':project_size, 'freelance_accounts':freelance_account})
