from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Company(models.Model):

    company_id = models.AutoField(primary_key=True)
    company_name =  models.CharField(max_length=50,null=True, blank=True,unique=True)

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,null=True, blank=True)
    password = models.CharField(max_length=50,null=True, blank=True)
    role = models.IntegerField()
    email = models.CharField(max_length =50,null=True, blank=True,unique=True)
    phone_number = models.CharField(max_length = 50,null=True, blank=True,unique=True)

class Product(models.Model):

    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50,null=True, blank=True)
    date_added = models.DateTimeField()
    quantity = models.IntegerField()
    description = models.CharField(max_length=1000,null=True, blank=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    def as_dict(self):
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "date_added" : self.date_added,
            "quantity" : self.quantity,
            "description" : self.description,
            "company_id" : self.company.company_id,
            "company_name": self.company.company_name
        }

class Review(models.Model):

    review_id = models.AutoField(primary_key=True)
    review_text = models.CharField(max_length=1000,null=True, blank=True)
    review_date = models.DateTimeField()
    rate = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    companies = models.ManyToManyField(Company)
    products = models.ManyToManyField(Product)

class PurchaseOrder(models.Model):
    purchase_order_id = models.AutoField(primary_key=True)
    purchase_order_date = models.DateTimeField()
    purchase_order_status = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(3)])
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    purchase_quantity = models.IntegerField()
    products = models.ManyToManyField(Product)

class SaleOrder(models.Model):
    sale_order_id = models.AutoField(primary_key=True)
    sale_order_date = models.DateTimeField()
    sale_order_status = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    account = models.ForeignKey(Account,on_delete= models.CASCADE)
    purchase_order = models.OneToOneField(PurchaseOrder,on_delete=models.CASCADE)

class ReceiptOrder(models.Model):
    receipt_order_id = models.AutoField(primary_key=True)
    receipt_order_date = models.DateTimeField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    sale_order = models.OneToOneField(SaleOrder,on_delete=models.CASCADE)








