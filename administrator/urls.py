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

app_name = 'administrator'
urlpatterns = [
    url(r'^dashboard/$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^add_freelance_account/$', views.redirect_to_add_freelance_account, name='redirect_to_add_freelance_account'),
    url(r'^upwork_account/$', views.upwork_account, name='upwork_account'),
    url(r'^guru_account/$', views.guru_account, name='guru_account'),
    url(r'^admin_account/$', views.admin_account, name='admin_account'),
    url(r'^bde_account/$', views.bde_account, name='bde_account'),
    url(r'^tl_account/$', views.tl_account, name='tl_account'),
    url(r'^employee_account/$', views.employee_account, name='employee_account'),
    url(r'^applied_jobs/$', views.applied_jobs, name='applied_jobs'),
]
