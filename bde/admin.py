from django.contrib import admin
from .models import ProjectSize, Contract, LeadGeneratedContract, SalesContract

# Register your models here.
admin.site.register(ProjectSize)
admin.site.register(Contract)
admin.site.register(LeadGeneratedContract)
admin.site.register(SalesContract)