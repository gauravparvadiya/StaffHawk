from django.shortcuts import render, redirect
from .models import ProjectSize, Contract, LeadGeneratedContract, SalesContract
from administrator.models import FreelanceAccount, Technology, TechType
from Authentication.models import User
from django.core.files.storage import FileSystemStorage
import os
from datetime import datetime

def index(request):
    if request.session.has_key('username'):
        return render(request, "bde/dashboard.html")
    else:
        return redirect("/")


def add_application(request):
    if request.session.has_key('username'):
        project_size = ProjectSize.objects.all()
        freelance_account = FreelanceAccount.objects.all()
        return render(request, "bde/add_application.html",
                      {'project_sizes': project_size, 'freelance_accounts': freelance_account})
    else:
        return redirect("/")


def add_application_form_submission(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            if 'attachment' in request.FILES:
                print("in if")
                attachment = request.FILES['attachment']
                fs = FileSystemStorage()
                ext = os.path.splitext(attachment.name)[1]
                ext = ext.lower()
                print(ext)
                date = datetime.now()
                result = '%s%s%s%s%s%s_%s' % (date.year, date.month, date.day, datetime.hour, datetime.minute, date.second, os.urandom(10).hex())
                print(result)
                filename = fs.save(result + ext, attachment)
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
            project_type = request.POST['payment_method']
            project_amount = request.POST['project_amount']
            bde_user = User.objects.get(user_email=request.session['username'])

            if invited_by_client == '1':
                new_job_application = Contract(project_title=project_title, project_url=project_url,
                                               project_size_id=project_size, freelance_account_id=freelance_account,
                                               invited_by_client=invited_by_client, project_attachment=upload_file_url,
                                               client_location=client_location, project_desc=project_description,
                                               contract_type=project_type, contract_price=project_amount,
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
                                               contract_type=project_type, contract_price=project_amount,
                                               bidder_account_id=bde_user.id)
                new_job_application.save()
                return redirect('/bde/applied_jobs')
        else:
            return redirect('/bde/add_application')
    else:
        return redirect("/")


def applied_jobs(request):
    if request.session.has_key('username'):
        bde_user = User.objects.get(user_email=request.session['username'])
        jobs_list = Contract.objects.filter(bidder_account_id=bde_user.id)
        return render(request, "bde/applied_jobs.html", {'jobs_lists': jobs_list})
    else:
        return redirect("/")


def lead_generated_jobs(request):
    if request.session.has_key('username'):
        bde_user = User.objects.get(user_email=request.session['username'])
        job_list = Contract.objects.filter(lead_generated='1', sales_converted='0', bidder_account_id=bde_user.id,
                                           leadgeneratedcontract__bidder_account_id=bde_user.id).values(
            'project_size__size',
            'project_url',
            'project_title',
            'project_desc',
            'client_location',
            'freelance_account__name_on_account',
            'leadgeneratedcontract__follow_up_time', 'lead_generated', 'sales_converted', 'contract_price',
            'contract_type',
            'id')
        return render(request, "bde/lead_generated_jobs.html", {'jobs_lists': job_list})
    else:
        return redirect("/")


def set_lead_generated(request):
    if request.session.has_key('username'):
        print(request.POST['check'])
        bde_user = User.objects.get(user_email=request.session['username'])
        update_contract_tbl = Contract.objects.get(id=request.POST['check'])
        update_contract_tbl.lead_generated = '1'
        update_contract_tbl.save()
        lead_generated = LeadGeneratedContract(lead_contract_id=update_contract_tbl.id,
                                               bidder_account_id=bde_user.id)
        lead_generated.save()
        # print(update_contract_tbl)
        jobs_list = Contract.objects.filter(bidder_account_id=bde_user.id)
        return render(request, "bde/applied_jobs.html", {'jobs_lists': jobs_list})
    else:
        return redirect("/")


def remove_lead_generated(request):
    if request.session.has_key('username'):
        print(request.POST['check'])
        update_contract_tbl = Contract.objects.get(id=request.POST['check'])
        update_contract_tbl.lead_generated = '0'
        update_contract_tbl.save()
        remove_lead = LeadGeneratedContract.objects.get(lead_contract_id=update_contract_tbl.id)
        remove_lead.delete()
        bde_user = User.objects.get(user_email=request.session['username'])
        jobs_list = Contract.objects.filter(bidder_account_id=bde_user.id)
        return render(request, "bde/applied_jobs.html", {'jobs_lists': jobs_list})
    else:
        return redirect("/")


def set_sales_generated(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            list_str = ",".join(request.POST.getlist('technology_list'))
            project_type = request.POST['payment_method']
            project_amount = request.POST['project_amount']
            freelance_account = request.POST['freelance_account']
            contract_id = request.POST['contract_id']

            # updated Contract schema
            contract_tbl_record = Contract.objects.get(id=contract_id)
            contract_tbl_record.sales_converted = '1'
            contract_tbl_record.save()

            # create new entry on SalesContract schema
            bde_user = User.objects.get(user_email=request.session['username'])
            sales_contract = SalesContract(contract_payment_type=project_type, contract_total_amount=project_amount,
                                           freelance_account_id=freelance_account, sales_bde_id=bde_user.id,
                                           technology_id=list_str, sales_contract_id=contract_id)
            sales_contract.save()
            return redirect('/bde/sales_generated_jobs')
        else:
            return redirect('/bde/set_sales_generated')
    else:
        return redirect("/")


def sales_generated_jobs(request):
    if request.session.has_key('username'):
        bde_user = User.objects.get(user_email=request.session['username'])
        # sales_info = SalesContract.objects.all()
        jobs_list = Contract.objects.filter(bidder_account_id=bde_user.id, lead_generated='1', sales_converted='1',
                                            salescontract__sales_bde_id=bde_user.id).values('project_size__size',
                                                                                            'project_title',
                                                                                            'project_desc',
                                                                                            'project_url',
                                                                                            'freelance_account__name_on_account',
                                                                                            'salescontract__contract_payment_type',
                                                                                            'salescontract__contract_total_amount',
                                                                                            'client_location')
        return render(request, "bde/sales_generated_jobs.html", {'jobs_lists': jobs_list})
    else:
        return redirect("/")


def add_sales_info(request):
    if request.session.has_key('username'):
        contract = Contract.objects.get(id=request.GET['id'])
        freelance_account = FreelanceAccount.objects.all()
        technology = Technology.objects.all()
        techtype = TechType.objects.all()
        return render(request, "bde/add_sales_info.html",
                      {'contract': contract, 'freelance_accounts': freelance_account, 'technologies': technology,
                       'techtypes': techtype})
    else:
        return redirect("/")
