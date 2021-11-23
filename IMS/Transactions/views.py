import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Accounts.models import Account
from Products.models import Product
from Transactions.models import PurchaseOrder


def getPurchaseOrders(request):
    purchaseOrders = PurchaseOrder.objects.all()
    json_purchaseOrders = list()
    for purchase_order in purchaseOrders:
        json_purchaseOrders.append(json.dumps(purchase_order.as_dict()))
    return HttpResponse(json.dumps(json_purchaseOrders))

def makePurchaseOrder(request):
    purchaseOrderData = json.loads(request.body)
    purchase_order_id = purchaseOrderData["purchase_order_id"]
    purchase_order_date = purchaseOrderData["purchase_order_date"]
    purchase_order_status = purchaseOrderData["purchase_order_status"]
    purchase_quantity = purchaseOrderData["purchase_quantity"]
    account_id = purchaseOrderData["account_id"]
    products = purchaseOrderData["products"]
    account = Account.objects.filter(account_id = account_id).first()
    purchaseOrder = PurchaseOrder(purchase_order_id = purchase_order_id , purchase_order_date = purchase_order_date
                                  ,purchase_order_status = purchase_order_status,purchase_quantity = purchase_quantity
                                  ,account = account)
    for product in products:
        productModel = Product.objects.filter(product_id=product["product_id"]).first()
        purchaseOrder.products.add(productModel)

    purchaseOrder.save()
    return HttpResponse("Purchase order made.")

def modifyPurchaseOrder(request):
    purchaseOrderData = json.loads(request.body)
    purchase_order_id = purchaseOrderData["purchase_order_id"]
    purchaseOrder = PurchaseOrder.objects.filter(purchase_order_id = purchase_order_id).first()
    account_id = purchaseOrderData["account_id"]
    if account_id == purchaseOrder.account.account_id:
        purchase_order_date = purchaseOrderData["purchase_order_date"]
        purchase_order_status = purchaseOrderData["purchase_order_status"]
        purchase_quantity = purchaseOrderData["purchase_quantity"]
        products = purchaseOrderData["products"]
        for product in products:
            productModel = Product.objects.filter(product_id=product["product_id"]).first()
            purchaseOrder.products.add(productModel)
        purchaseOrder.save()
        return HttpResponse("Purchase order modified.")

    else:
        return HttpResponse("You have no permissions for such operation.")

def removePurchaseOrder(request):
    purchaseOrderData = json.loads(request.body)
    purchase_order_id = purchaseOrderData["purchase_order_id"]
    PurchaseOrder.objects.filter(purchase_order_id = purchase_order_id).delete()
    return HttpResponse("Purchase order removed.")


