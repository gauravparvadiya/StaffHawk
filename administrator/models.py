from django.db import models

# Create your models here.


class FreelanceAccount(models.Model):
    name_on_account = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    profile_link = models.CharField(max_length=200)
    account_type = models.CharField(max_length=3) # 1.Upwork 2. Guru
    account_profile_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name_on_account

