from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name ='home'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('products/', views.products_view, name='products'),
    path('cart/',views.cart,name='cart'),
    path('cart_status/', views.cart_status, name='cart_status'),
    path('products/<slug:slug>/', views.products_view, name='products_by_category'),
   
    path('login/',views.login_user,name='login'),
    path('register/', views.register, name='register'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('logout/', views.logout_user, name='logout'),
    path('update_order/', views.update_order, name='update_order'),
    path('search/', views.search, name='search'),
    path('checkout/', views.checkout, name='checkout'), 
]
