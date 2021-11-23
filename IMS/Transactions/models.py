from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class PurchaseOrder(models.Model):
    purchase_order_id = models.AutoField(primary_key=True)
    purchase_order_date = models.DateTimeField(null=True, blank=True)
    purchase_order_status = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    account = models.ForeignKey("Accounts.Account", on_delete=models.CASCADE,null=True, blank=True)
    purchase_quantity = models.IntegerField(null=True, blank=True)
    products = models.ManyToManyField("Products.Product",null=True, blank=True)

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
    account = models.ForeignKey("Accounts.Account", on_delete=models.CASCADE,null=True, blank=True)
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
    account = models.ForeignKey("Accounts.Account", on_delete=models.CASCADE,null=True, blank=True)
    sale_order = models.OneToOneField(SaleOrder, on_delete=models.CASCADE,null=True, blank=True)

    def as_dict(self):
        return {
            "receipt_order_id": self.receipt_order_id,
            "receipt_order_date": self.receipt_order_date,
            "account_id": self.account.account_id,
            "sale_order_id": self.sale_order.sale_order_id,
            "cost": self.sale_order.purchase_order.as_dict()["purchase_cost"]
        }