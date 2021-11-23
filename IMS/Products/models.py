from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50, null=True, blank=True, unique=True)

    def as_dict(self):
        return {
            "company_id": self.company_id,
            "company_name": self.company_name
        }


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50, null=True, blank=True)
    product_price = models.FloatField(null=True, blank=True)
    date_added = models.DateTimeField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True, blank=True)

    def as_dict(self):
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "product_price": self.product_price,
            "date_added": self.date_added,
            "quantity": self.quantity,
            "description": self.description,
            "company_id": self.company.company_id,
            "company_name": self.company.company_name
        }