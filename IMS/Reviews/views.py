import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from IMS.Accounts.models import Account
from IMS.Products.models import Product, Company
from IMS.Reviews.models import Review


def addProdcutReview(request):
    productReviewData = json.load(request.body)
    review_text = productReviewData['review_text']
    review_date =  productReviewData['review_date']
    rate = productReviewData['rate']
    account_id = productReviewData['account_id']
    account = Account.objects.filter(account_id = account_id).first()
    product_id = productReviewData['product_id']
    product = Product.objects.filter(product_id = product_id).first()
    review = Review(review_text = review_text,review_date = review_date,rate = rate,
                    account = account,company = None,product = product)
    review.save()
    return HttpResponse('Product review added.')


def addCompanyReview(request):
    companyReviewData = json.load(request.body)
    review_text = companyReviewData['review_text']
    review_date =  companyReviewData['review_date']
    rate = companyReviewData['rate']
    account_id = companyReviewData['account_id']
    account = Account.objects.filter(account_id = account_id).first()
    company_id = companyReviewData['company_id']
    company = Company.objects.filter(company_id = company_id).first()
    review = Review(review_text = review_text,review_date = review_date,rate = rate,
                    account = account,company = company,product = None)
    review.save()
    return HttpResponse('Company review added.')

def removeReview(request):
    productReviewData = json.load(request.body)
    review_id = productReviewData['review_id']
    Review.objects.filter(review_id = review_id).first().delete()
    return HttpResponse('Review removed.')

def modifyReview(request):
    productReviewData = json.load(request.body)
    review_id = productReviewData['review_id']
    review_text = productReviewData['review_text']
    rate = productReviewData['rate']
    review = Review.objects.filter(review_id = review_id).first()
    review.review_text = review_text
    review.rate = rate
    review.save()
    return HttpResponse('Review modified.')

def getReview(request):
    productReviewData = json.load(request.body)
    review_id = productReviewData['review_id']
    review = Review.objects.filter(review_id = review_id).first()
    return HttpResponse(json.dumps(review.as_dict()))

def getProductReviews(request):
    productReviewData = json.load(request.body)
    product_id = productReviewData['product_id']
    product = Product.objects.filter(product_id=product_id).first()
    reviews = Review.objects.filter(product = product).all()
    json_reviews = list()
    for review in reviews:
        json_reviews.append(json.dumps(review.as_dict()))
    return  HttpResponse(json.dumps(json_reviews))

def getCompanyReviews(request):
    productReviewData = json.load(request.body)
    company_id = productReviewData['company_id']
    company = Company.objects.filter(company_id=company_id).first()
    reviews = Review.objects.filter(company = company).all()
    json_reviews = list()
    for review in reviews:
        json_reviews.append(json.dumps(review.as_dict()))
    return  HttpResponse(json.dumps(json_reviews))








