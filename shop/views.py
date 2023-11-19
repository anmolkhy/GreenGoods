from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from .models import *

# Create your views here.
def check_login(request):
    if not request.user.is_authenticated:
        return redirect('login')

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def blog(request):
    return render(request, 'blog.html')

def clothing(request):
    items = Item.objects.filter(category='Clothing')
    return render(request, 'clothing.html' , {'items': items})

def beauty(request):
    items = Item.objects.filter(category='Beauty & Skin Care')
    return render(request, 'beauty.html', {'items': items})

def homekitchen(request):
    items = Item.objects.filter(category='Home & Kitchen')
    return render(request, 'homekitchen.html', {'items': items})

def accessories(request):
    items = Item.objects.filter(category='Accessories')
    return render(request, 'accessories.html', {'items': items})

def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    items = CartObject.objects.all()
    sum = 0
    for item in items:
        sum += item.item.discount_price * item.quantity
    if request.method == "POST":
        
        for n in items:
            n.quantity = int(request.POST[str(n.id)])
            n.save()
        return redirect('cart')
    return render(request, 'cart.html', {'items': items, 'sum': sum})
        
def loginuser(request):
    if request.method == "POST":
        #code for login
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', { 'message' : 'Invalid Credentials'})
    return render(request, 'login.html')

def save_order(request):
    if not request.user.is_authenticated:
        return redirect('login')
    cart_objects = CartObject.objects.all()
    sum = 0
    for obj in cart_objects:
        sum += obj.item.discount_price * obj.quantity
    date = datetime.now()
    order = Order.objects.create(user=request.user, ordered_date=date, price=sum)
    order.items.set(cart_objects.values_list('id', flat=True))
    order.price = sum
    order.save()
    CartObject.objects.all().delete()
    return redirect('index')

def product(request, product_slug):
    product = Item.objects.get(slug=product_slug)
    #code for adding item to cart
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')
        qty = request.POST['qty']
        ItemInventory.objects.create(item=product, quantity=qty, user=request.user)
        CartObject.objects.create(item=product, quantity=qty, user=request.user)
        return redirect('cart')
    return render(request, 'product.html', {'product': product})

def delete(request, item):
    item = CartObject.objects.get(id=int(item))
    item.delete()
    return redirect('cart')

def signup(request):
    if request.method == "POST":
        #code for signup
        username = request.POST['username'] 
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password != confirmpassword:
            return render(request, 'signup.html', {'message': 'Passwords do not match'})
        #check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'message': 'Username already exists'})
        #check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'message': 'Email already exists'})
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')

def logoutuser(request):
    logout(request)
    return redirect('index')

def orders(request):
    if not request.user.is_authenticated:
        return redirect('login')
    orders = Order.objects.filter(user=request.user)
    sum = 0
    for order in orders:
        sum += order.price
    return render(request, 'orders.html', {'orders': orders, 'sum': sum})

def order_details(request, order_id):
    if not request.user.is_authenticated:
        return redirect('login')
    order = Order.objects.get(id=int(order_id))
    items = order.items.all()
    return render(request, 'order_details.html', {'order': order, 'items': items})