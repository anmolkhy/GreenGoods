from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('base/', base, name='base'),
    path('blog/', blog, name='blog'),
    path('clothing/', clothing, name='clothing'),
    path('beauty/', beauty, name='beauty'),
    path('homekitchen/', homekitchen, name='homekitchen'),
    path('accessories/', accessories, name='accessories'),
    path('cart/', cart, name='cart'),
    path('login/', loginuser, name='login'),
    path('product/<slug:product_slug>', product, name='product'),
    path('delete/<item>', delete, name='delete'),
    path('logout/', logoutuser, name='logout'),
    path('saveorder/', save_order, name='saveorder'),
    path('orders/', orders, name='orders'),
    path('signup/', signup , name='signup'),
    path('order-detail/<str:order_id>', order_details, name='orderdetail'),
]
