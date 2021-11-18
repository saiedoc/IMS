from django.core.validators import MinValueValidator, MaxValueValidator
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


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    role = models.IntegerField()
    email = models.CharField(max_length=50, null=True, blank=True, unique=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True, unique=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null= True,blank=True)

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


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    review_text = models.CharField(max_length=1000, null=True, blank=True)
    review_date = models.DateTimeField(null=True, blank=True)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    account = models.ForeignKey(Account, on_delete=models.CASCADE,null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True, blank=True)

    def as_dict(self):
        return {
            "review_id": self.review_id,
            "review_text": self.review_text,
            "review_date": self.review_date,
            "rate": self.rate,
            "account": self.account.username,
            "product_id": self.product.product_id,
            "product_name": self.product.product_name
        }


class PurchaseOrder(models.Model):
    purchase_order_id = models.AutoField(primary_key=True)
    purchase_order_date = models.DateTimeField(null=True, blank=True)
    purchase_order_status = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    account = models.ForeignKey(Account, on_delete=models.CASCADE,null=True, blank=True)
    purchase_quantity = models.IntegerField(null=True, blank=True)
    products = models.ManyToManyField(Product,null=True, blank=True)

    def as_dict(self):
        PO = {
            "purchase_order_id": self.purchase_order_id,
            "purcahse_order_date": self.purchase_order_date,
            "purchase_order_status": self.purchase_order_status,
            "account_id": self.account.account_id,
            "purchase_quantity": self.purchase_quantity,
            "products": [],
            "purchase_cost": 0
        }

        for product in self.products.all():
            PO["products"].append(product.as_dict())
            PO["purchase_cost"] += product.product_price

        return PO


class SaleOrder(models.Model):
    sale_order_id = models.AutoField(primary_key=True)
    sale_order_date = models.DateTimeField(null=True, blank=True)
    sale_order_status = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)],null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE,null=True, blank=True)
    purchase_order = models.OneToOneField(PurchaseOrder, on_delete=models.CASCADE,null=True, blank=True)

    def as_dict(self):
        return {
            "sale_order_id": self.sale_order_id,
            "sale_order_date": self.sale_order_date,
            "sale_order_status": self.sale_order_status,
            "account_id": self.account.account_id,
            "purchase_order_id": self.purchase_order.purchase_order_id
        }


class ReceiptOrder(models.Model):
    receipt_order_id = models.AutoField(primary_key=True)
    receipt_order_date = models.DateTimeField(null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE,null=True, blank=True)
    sale_order = models.OneToOneField(SaleOrder, on_delete=models.CASCADE,null=True, blank=True)

    def as_dict(self):
        return {
            "receipt_order_id": self.receipt_order_id,
            "receipt_order_date": self.receipt_order_date,
            "account_id": self.account.account_id,
            "sale_order_id": self.sale_order.sale_order_id,
            "cost": self.sale_order.purchase_order.as_dict()["purchase_cost"]
        }
