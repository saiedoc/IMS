import json

from django.forms import model_to_dict
from django.http import HttpResponse

# Create your views here.
from django.utils.datetime_safe import datetime

from .models import Company, Account, Product, PurchaseOrder


def checkAdminPermission(account_id):
    account = Account.objects.filter(account_id = account_id).first()
    if account.role == 1:
        return True
    else:
        return False


def signUp(request):
    signUpData = json.loads(request.body)
    company_name = signUpData["company_name"]
    username = signUpData["username"]
    email = signUpData["email"]
    phone_number = signUpData["phone_number"]
    password = signUpData["password"]
    confirm_password = signUpData["confirm_password"]
    if password == confirm_password:
        company = Company(company_name=company_name)
        company.save()
        if  signUpData["role"] == "1":
            account = Account(username=username, email=email, phone_number=phone_number, password=password, company=company,
                          role=1)
        elif signUpData["role"] == "2":
            account = Account(username=username, email=email, phone_number=phone_number, password=password,
                              company=company,
                              role=2)
        elif signUpData["role"] == "3":
            account = Account(username=username, email=email, phone_number=phone_number, password=password,
                              company=company,
                              role=3)
        account.save()
        return HttpResponse("Signed Up")
    elif password != confirm_password:
        return HttpResponse("Passwords don't match")
    else:
        return HttpResponse("error occurred.")


def login(request):
    loginData = json.loads(request.body)
    username = loginData["username"]
    password = loginData["password"]
    account = Account.objects.filter(username = username,password = password).first()
    dict_obj = model_to_dict(account)
    jsonAccount = json.dumps(dict_obj)
    return HttpResponse(jsonAccount)

def getProducts(request):
    productsQS = Product.objects.all()
    products = productsQS.values()
    json_products = json.dumps(products)
    return HttpResponse(json_products)

def addProduct(request):
    productData = json.loads(request.body)
    account_id = productData["account_id"]
    product_name = productData["product_name"]
    date_added = datetime.now()
    quantity = productData["quantity"]
    description = productData["description"]
    company_name = productData["company_name"]
    if checkAdminPermission(account_id):
        company = Company.objects.filter(company_name=company_name).first()
        product = Product(product_name = product_name,date_added = date_added,quantity = quantity,description = description,company = company)
        product.save()
        return HttpResponse("Product added.")
    else:
        return HttpResponse("You have no permissions for such operation.")

def removeProduct(request):
    productData = json.loads(request.body)
    account_id = productData["account_id"]
    product_id = productData["product_id"]
    if checkAdminPermission(account_id):
        Product.objects.filter(product_id = product_id).delete()
        return HttpResponse("Product removed.")
    else:
        return HttpResponse("You have no permissions for such operation.")

def modifyProduct(request):
    productData = json.loads(request.body)
    account_id = productData["account_id"]
    product_id = productData["product_id"]
    product_name = productData["product_name"]
    date_added = productData["date_added"]
    quantity = productData["quantity"]
    description = productData["description"]
    if checkAdminPermission(account_id):
        Product.objects.filter(product_id = product_id).update(product_name = product_name,date_added = date_added,quantity = quantity,description = description)
        return HttpResponse("Product updated.")
    else:
        return HttpResponse("You have no permissions for such operation.")

def updateStock(request):
    productData = json.loads(request.body)
    product_id = productData["product_id"]
    quantity = productData["quantity"]
    Product.objects.filter(product_id = product_id).update(quantity = quantity)
    return HttpResponse("Stock updated.")


def getPurchaseOrders(request):
    purchaseOrders = PurchaseOrder.objects.all()
    dict_products = model_to_dict(purchaseOrders)
    json_products = json.dumps(dict_products)
    return HttpResponse(json_products)

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
    return HttpResponse("Purcahse order deleted.")























