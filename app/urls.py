from django.contrib import admin
from django.urls import path,include

from app.views import  about, contact, IndexVIew, registerPage, loginPage, ProductView

urlpatterns = [
    path('', IndexVIew.as_view(), name='index'),
    path('products/', ProductView.as_view(), name='products'),
    path('about/', about, name='about'),
    path('contacct/', contact, name='contact'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
]