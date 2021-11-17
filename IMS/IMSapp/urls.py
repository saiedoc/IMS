from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signUp, name='signup'),
    path('login', views.login, name='login'),
    path('addProduct',views.addProduct,name = 'addProduct'),
    path('getProducts',views.getProducts,name = 'getProducts'),
    path('removeProduct',views.removeProduct,name = 'removeProduct'),
    path('modifyProduct',views.modifyProduct,name = 'modifyProduct'),
    path('updateStock',views.updateStock,name = 'updateStock'),
    path('makePurchaseOrder',views.makePurchaseOrder,name = 'makePurchaseOrder'),
    path('removePurchaseOrder',views.removePurchaseOrder,name= 'removePurchaseOrder'),
    path('modifyPurchaseOrder',views.modifyPurchaseOrder,name = 'modifyPurchaseOrder')

]