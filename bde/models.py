from django.db import models
from datetime import datetime, timedelta


class ProjectSize(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size


class Contract(models.Model):
    project_title = models.CharField(max_length=500)
    project_url = models.URLField(max_length=200)
    project_size = models.ForeignKey(ProjectSize, on_delete=models.CASCADE)
    project_desc = models.TextField()
    project_attachment = models.FileField(max_length=200)
    client_location = models.CharField(max_length=200)
    invited_by_client = models.CharField(max_length=5)
    lead_generated = models.CharField(max_length=5, default='0')
    sales_converted = models.CharField(max_length=5, default='0')
    contract_type = models.CharField(max_length=3, default='1')
    contract_price = models.CharField(
        max_length=10)  # Hour rate in case of Hourly contract otherwise fixed price.
    freelance_account = models.ForeignKey('administrator.FreelanceAccount', on_delete=models.CASCADE)
    bidder_account = models.ForeignKey('Authentication.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contract_status = models.CharField(max_length=3,default='0')  # 0.Active 1.Rejected
    today_follow_up = models.CharField(max_length=3, default='0')

    def __str__(self):
        return self.project_title


class LeadGeneratedContract(models.Model):
    lead_contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    bidder_account = models.ForeignKey('Authentication.User', on_delete=models.CASCADE)
    follow_up_time = models.DateTimeField(default=datetime.now() + timedelta(days=2))
    next_follow_up_time = models.DateTimeField(default=datetime.now() + timedelta(days=2))
    follow_up_counter = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lead_contract.project_title


class SalesContract(models.Model):
    sales_contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    sales_bde = models.ForeignKey('Authentication.User', on_delete=models.CASCADE)
    freelance_account = models.ForeignKey('administrator.FreelanceAccount', on_delete=models.CASCADE)
    contract_payment_type = models.CharField(max_length=3)  # 1.Hourly 2.Fixed
    contract_total_amount = models.CharField(
        max_length=10)  # Hour rate in case of Hourly contract otherwise fixed price.
    technology_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sales_contract.project_title
