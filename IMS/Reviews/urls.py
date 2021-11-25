from django.urls import path

from . import views

urlpatterns = [

    path('addProductReview',views.addProdcutReview,name ='addProductReview'),
    path('addCompanyReview', views.addCompanyReview, name='addCompanyReview'),
    path('removeReview', views.removeReview, name='removeReview'),
    path('modifyReview', views.modifyReview, name='modifyReview')

]