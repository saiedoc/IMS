import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Accounts.models import Account
from Products.models import Product
from Transactions.models import PurchaseOrder, SaleOrder, ReceiptOrder


def getPurchaseOrders(request):
    purchaseOrders = PurchaseOrder.objects.filter(purchase_order_status = 1).all()
    json_purchaseOrders = list()
    for purchase_order in purchaseOrders:
        json_purchaseOrders.append(json.dumps(purchase_order.as_dict()))
    return HttpResponse(json.dumps(json_purchaseOrders))

def makePurchaseOrder(request):
    purchaseOrderData = json.loads(request.body)
    purchase_order_date = purchaseOrderData["purchase_order_date"]
    purchase_order_status = purchaseOrderData["purchase_order_status"]
    purchase_quantity = purchaseOrderData["purchase_quantity"]
    account_id = purchaseOrderData["account_id"]
    products = purchaseOrderData["products"]
    account = Account.objects.filter(account_id = account_id).first()
    purchaseOrder = PurchaseOrder(purchase_order_date = purchase_order_date
                                  ,purchase_order_status = purchase_order_status,purchase_quantity = purchase_quantity
                                  ,account = account)
    for product in products:
        productModel = Product.objects.filter(product_id=product["product_id"]).first()
        productModel.quantity = product.quantity
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
        purchaseOrder.products.clear()
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

def getSaleOrders(request):
    saleOrders = SaleOrder.objects.filter(sale_order_status = 1).all()
    jsonSaleOrders = list()
    for saleOrder in saleOrders:
        jsonSaleOrders.append(json.dumps(saleOrder.as_dict()))
    return HttpResponse(json.dumps(jsonSaleOrders))

def makeSaleOrder(request):
    saleOrderData = json.loads(request.body)
    sale_order_date = saleOrderData['sale_order_date']
    account_id = saleOrderData['account_id']
    account = Account.objects.filter(account_id = account_id).first()
    purchase_order_id = saleOrderData['purchase_order_id']
    purchaseOrder = PurchaseOrder.objects.filter(purchase_order_id = purchase_order_id).first()
    purchaseOrder.purchase_order_status = 2
    for product in purchaseOrder.products:
        original_product = Product.objects.filter(product_id = product.product_id).first()
        original_product.quantity = original_product.quantity - product.quantity
        original_product.save()

    saleOrder = SaleOrder(sale_order_date = sale_order_date,
                          sale_order_status = 1,account = account,purchase_order = purchaseOrder)
    saleOrder.save()
    purchaseOrder.save()
    return HttpResponse('Sale order made')

def removeSaleOrder(request):
    saleOrderData = json.loads(request.body)
    sale_order_id = saleOrderData['sale_order_id']
    saleOrder = SaleOrder.objects.filter(sale_order_id = sale_order_id).first()
    for product in saleOrder.purchase_order.products:
        original_product = Product.objects.filter(product_id=product.product_id).first()
        original_product.quantity = original_product.quantity + product.quantity
        original_product.save()
    SaleOrder.objects.filter(sale_order_id=sale_order_id).delete()
    return HttpResponse('Sale order removed')

def getReciptOrders(request):
    receiptOrders = ReceiptOrder.objects.filter.all()
    jsonReceiptOrders = list()
    for receiptOrder in receiptOrders:
        jsonReceiptOrders.append(json.dumps(receiptOrder.as_dict()))
    return HttpResponse(json.dumps(jsonReceiptOrders))

def makeReceiptOrder(request):
    receiptOrderData = json.loads(request.body)
    receipt_order_date = receiptOrderData['receipt_order_date']
    account_id = receiptOrderData['account_id']
    account = Account.objects.filter(account_id = account_id).first()
    sale_order_id = receiptOrderData['sale_order_id']
    saleOrder = SaleOrder.objects.filter(sale_order_id = sale_order_id).first()
    saleOrder.sale_order_status = 2
    receiptOrder = ReceiptOrder(receipt_order_date = receipt_order_date,
                                account = account,sale_order = saleOrder)




