from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Review(models.Model):

    review_id = models.AutoField(primary_key=True)
    review_text = models.CharField(max_length=1000, null=True, blank=True)
    review_date = models.DateTimeField(null=True, blank=True)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    account = models.ForeignKey("Accounts.Account", on_delete=models.CASCADE,null=True, blank=True)
    company = models.ForeignKey("Products.Company", on_delete=models.CASCADE,null=True, blank=True)
    product = models.ForeignKey("Products.Product", on_delete=models.CASCADE,null=True, blank=True)

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

