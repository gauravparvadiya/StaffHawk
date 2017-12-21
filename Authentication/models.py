from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_role = models.CharField(max_length=3)  # 1.Admin 2.BIDDER 3.TL 4.Employee
    user_gender = models.CharField(max_length=10)
    auth_token = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name