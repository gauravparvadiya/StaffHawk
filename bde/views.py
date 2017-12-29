from django.shortcuts import render, redirect
from .models import ProjectSize, Contract, LeadGeneratedContract
from administrator.models import FreelanceAccount
from Authentication.models import User
from django.core.files.storage import FileSystemStorage
from django.core import serializers


def index(request):
    if request.session.has_key('username'):
        return render(request, "bde/dashboard.html")
    else:
        return render(request, "Authentication/login.html")


def add_application(request):
    project_size = ProjectSize.objects.all()
    freelance_account = FreelanceAccount.objects.all()
    return render(request, "bde/add_application.html",
                  {'project_sizes': project_size, 'freelance_accounts': freelance_account})


def add_application_form_submission(request):
    if request.method == 'POST':
        if 'attachment' in request.FILES:
            print("in if")
            attachment = request.FILES['attachment']
            fs = FileSystemStorage()
            filename = fs.save(attachment.name, attachment)
            upload_file_url = fs.url(filename)
        else:
            print("in else")
            upload_file_url = 'null'
        project_title = request.POST['project_title']
        project_url = request.POST['project_url']
        project_size = request.POST['project_size']
        freelance_account = request.POST['freelance_account']
        invited_by_client = request.POST['invited_by_client']
        client_location = request.POST['client_location']
        project_description = request.POST['project_description']
        bde_user = User.objects.get(user_email=request.session['username'])

        if invited_by_client == '1':
            new_job_application = Contract(project_title=project_title, project_url=project_url,
                                           project_size_id=project_size, freelance_account_id=freelance_account,
                                           invited_by_client=invited_by_client, project_attachment=upload_file_url,
                                           client_location=client_location, project_desc=project_description,
                                           bidder_account_id=bde_user.id, lead_generated='1')
            new_job_application.save()
            lead_generated = LeadGeneratedContract(lead_contract_id=new_job_application.id,
                                                   bidder_account_id=bde_user.id)
            lead_generated.save()
            return redirect('/bde/lead_generated_jobs/')
        else:
            new_job_application = Contract(project_title=project_title, project_url=project_url,
                                           project_size_id=project_size, freelance_account_id=freelance_account,
                                           invited_by_client=invited_by_client, project_attachment=upload_file_url,
                                           client_location=client_location, project_desc=project_description,
                                           bidder_account_id=bde_user.id)
            new_job_application.save()
            return redirect('/bde/applied_jobs')
    else:
        return redirect('/bde/add_application')


def applied_jobs(request):
    bde_user = User.objects.get(user_email=request.session['username'])
    jobs_list = Contract.objects.filter(bidder_account_id=bde_user.id)
    return render(request, "bde/applied_jobs.html", {'jobs_lists': jobs_list})


def lead_generated_jobs(request):
    bde_user = User.objects.get(user_email=request.session['username'])
    job_list = Contract.objects.filter(lead_generated='1', sales_converted='0', bidder_account_id=bde_user.id,
                                       leadgeneratedcontract__bidder_account_id=bde_user.id).values('project_size__size',
                                                                                                    'project_url',
                                                                                                    'project_title',
                                                                                                    'project_desc',
                                                                                                    'client_location',
                                                                                                    'freelance_account__name_on_account',
                                                                                                    'leadgeneratedcontract__follow_up_time')
    return render(request, "bde/lead_generated_jobs.html", {'jobs_lists': job_list})
