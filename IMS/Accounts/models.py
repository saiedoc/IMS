from django.db import models

# Create your models here.



class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    role = models.IntegerField()
    email = models.CharField(max_length=50, null=True, blank=True, unique=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True, unique=True)
    company = models.ForeignKey("Products.Company",on_delete=models.CASCADE,null= True,blank=True)

    def as_dict(self):
        return {
            "account_id": self.account_id,
            "username": self.username,
            "role": self.role,
            "email": self.email,
            "phone_number": self.phone_number,
            "company_id": self.company.company_id,
            "company_name": self.company.company_name
        }