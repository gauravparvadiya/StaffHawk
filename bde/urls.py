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
    # url(r'^administrator/employee_account/$', views.employee_account, name='employee_account'),
]
