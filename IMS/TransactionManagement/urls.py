from django.urls import path

from . import views

urlpatterns = [

    path('makePurchaseOrder',views.makePurchaseOrder,name = 'makePurchaseOrder'),
    path('removePurchaseOrder',views.removePurchaseOrder,name= 'removePurchaseOrder'),
    path('modifyPurchaseOrder',views.modifyPurchaseOrder,name = 'modifyPurchaseOrder')

]