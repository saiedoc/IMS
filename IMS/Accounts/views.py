import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Products.models import Company
from .models import Account

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
        company = Company.objects.filter(company_name = company_name).first()
        if  signUpData["role"] == 1:
            account = Account(username=username, email=email, phone_number=phone_number, password=password, company=company,
                          role=1)
            account.save()
        elif signUpData["role"] == 2:
            account = Account(username=username, email=email, phone_number=phone_number, password=password,
                              company=company,
                              role=2)
            account.save()
        elif signUpData["role"] == 3:
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
    jsonAccount = json.dumps(account.as_dict())
    return HttpResponse(jsonAccount)