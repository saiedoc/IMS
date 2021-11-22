from django.urls import path

from . import views

urlpatterns = [
    path('addProduct',views.addProduct,name = 'addProduct'),
    path('getProducts',views.getProducts,name = 'getProducts'),
    path('removeProduct',views.removeProduct,name = 'removeProduct'),
    path('modifyProduct',views.modifyProduct,name = 'modifyProduct'),
    path('updateStock',views.updateStock,name = 'updateStock')
]