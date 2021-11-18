# Generated by Django 3.2.9 on 2021-11-18 13:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IMSapp', '0003_auto_20211109_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='company',
        ),
        migrations.RemoveField(
            model_name='review',
            name='companies',
        ),
        migrations.RemoveField(
            model_name='review',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IMSapp.company'),
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IMSapp.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IMSapp.company'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IMSapp.account'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='IMSapp.Product'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='purchase_order_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='purchase_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='receiptorder',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IMSapp.account'),
        ),
        migrations.AlterField(
            model_name='receiptorder',
            name='receipt_order_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='receiptorder',
            name='sale_order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IMSapp.saleorder'),
        ),
        migrations.AlterField(
            model_name='review',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IMSapp.account'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='saleorder',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IMSapp.account'),
        ),
        migrations.AlterField(
            model_name='saleorder',
            name='purchase_order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IMSapp.purchaseorder'),
        ),
        migrations.AlterField(
            model_name='saleorder',
            name='sale_order_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='saleorder',
            name='sale_order_status',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)]),
        ),
    ]
