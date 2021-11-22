from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signUp, name='signup'),
    path('login', views.login, name='login'),
]