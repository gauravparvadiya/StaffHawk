from django.db import models

# Create your models here.


class FreelanceAccount(models.Model):
    name_on_account = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    profile_link = models.CharField(max_length=200)
    account_type = models.CharField(max_length=3) # 1.Upwork 2. Guru
    account_profile_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_on_account

    def natural_key(self):
        return self.name_on_account


class TechType(models.Model):
    technology_type_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.technology_type_name


class Technology(models.Model):
    technology_name = models.CharField(max_length=100)
    technology_type = models.ForeignKey(TechType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.technology_name


class TodayQuote(models.Model):
    quote_text = models.TextField()
    quote_author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.quote_text
