import json
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Accounts.views import checkAdminPermission
from .models import Product, Company


def getCompanyProducts(request):
    productData = json.loads(request)
    company_id = productData['company_id']
    company = Company.objects.filter(company_id = company_id).first()
    products = Product.objects.filter(company = company).all()
    json_products = list()
    for product in products:
        json_products.append(json.dumps(product.as_dict()))
    return HttpResponse(json.dumps(json_products))

def getProduct(request):
    productData = json.loads(request)
    product_id = productData['product_id']
    product = Product.objects.filter(product_id = product_id).first()
    return HttpResponse(json.dumps(product.as_dict()))

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