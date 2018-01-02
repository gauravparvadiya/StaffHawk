"""StaffHawk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.conf.urls import url

app_name = 'bde'
urlpatterns = [
    url(r'^dashboard/$', views.index, name='index'),
    url(r'^add_application/$', views.add_application, name='add_application'),
    url(r'^add_application_form_submission/$', views.add_application_form_submission, name='add_application_form_submission'),
    url(r'^applied_jobs/$', views.applied_jobs, name='applied_jobs'),
    url(r'^lead_generated_jobs/$', views.lead_generated_jobs, name='lead_generated_jobs'),
    url(r'^set_lead_generated/$', views.set_lead_generated, name='set_lead_generated'),
    url(r'^remove_lead_generated/$', views.remove_lead_generated, name='remove_lead_generated'),
    url(r'^set_sales_generated/$', views.set_sales_generated, name='set_sales_generated'),
    url(r'^sales_generated_jobs/$', views.sales_generated_jobs, name='sales_generated_jobs'),
    url(r'^add_sales_info/$', views.add_sales_info, name='add_sales_info'),
    url(r'^delete_job/$', views.delete_job, name='delete_job'),
    url(r'^edit_contract_info/$', views.edit_contract_info, name='edit_contract_info'),
    url(r'^edit_contract_info_form_submission/$', views.edit_contract_info_form_submission, name='edit_contract_info_form_submission'),
]
