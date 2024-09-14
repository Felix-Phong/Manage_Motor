from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from django.db.models import Count
from .models import *
from django.db import transaction
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password
import json


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        account = request.user
        order,created = Order.objects.get_or_create(account=account,status=0)
        orderDetails = order.orderdetail_set.all()
        cartItems = order.get_cart_items
    else:
        orderDetails = []
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    categories = Category.objects.all()
    best_selling_products = get_best_selling(8)
    latest_products = get_latest_products(8)
    
    context = {
        'best_selling_products': best_selling_products,
        'latest_products': latest_products,
        'categories': categories,
        'cartItems':cartItems,
    }
    return render(request, 'app/home.html', context)


def products_view(request, slug=None):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        account = request.user
        order,created = Order.objects.get_or_create(account=account,status=0)
        orderDetails = order.orderdetail_set.all()
        cartItems = order.get_cart_items
    else:
        orderDetails = []
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
   
    paginator = Paginator(products, 6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'cartItems':cartItems,
        'categories': categories,
        'products': products,
        'page_obj': page_obj,
    }
    return render(request, 'app/products.html', context)
def search(request, slug=None):
    categories = Category.objects.all()
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Product.objects.filter(name__contains = searched)
    if request.user.is_authenticated:
        account = request.user
        order,created = Order.objects.get_or_create(account=account,status=0)
        orderDetails = order.orderdetail_set.all()
        cartItems = order.get_cart_items
    else:
        orderDetails = []
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    categories = Category.objects.all()
    
    paginator = Paginator(keys, 6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories': categories,
        'searched':searched,
        'keys':keys,
        'cartItems':cartItems,
        'page_obj': page_obj,
    }
    return render(request, 'app/search.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    category = product.category
    reviews = OrderDetail.objects.filter(product=product, comment__isnull=False)
    average_rating = reviews.aggregate(models.Avg('rate'))['rate__avg'] or 0
    # check_order = OrderDetail.objects.filter(account=request.user, product=product).exists() if request.user.is_authenticated else False
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'product': product,
        'category': category,
        'reviews': reviews,
        'average_rating': average_rating,
        # 'check_order': check_order,
    }
    return render(request, 'app/product_detail.html', context)

def cart(request):
    if request.user.is_authenticated:
        account = request.user
        order, created = Order.objects.get_or_create(account=account,status = 0)
        order_details = order.orderdetail_set.all()
        cartItems = order.get_cart_items
    else:
        return redirect('login')
    categories = Category.objects.all()

    context={'order_details':order_details,'order':order, 'cartItems':cartItems,'categories': categories,}
    return render(request,'app/cart.html',context)

    #  return redirect('login')
    
def cart_status(request):
    account = request.user
    order_details = OrderDetail.objects.filter(account=account, status__in=[2, 3, 4]).select_related('product')
    categories = Category.objects.all()

    context = {
        'order_details': order_details,
        'categories': categories,
    }
    return render(request, 'app/cart_status.html', context)
def user_profile(request):
    context={}
    return render(request,'app/user_profile.html',context)
def logout_user(request):
    logout(request)
    return redirect('login')
def login_user(request):
    categories = Category.objects.all()  
    
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: messages.info(request,'Tên đăng nhập hoặc mật khẩu chưa dúng')
    context = {'categories': categories}
    return render(request, 'app/login.html', context)



def register(request):
    categories = Category.objects.all()  
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'categories': categories,'form':form}
    

    return render(request, 'app/register.html',context)


def checkout(request):
    account = request.user

    if request.method == 'POST' and 'buy_order' in request.POST:
        check = True
        order_details = OrderDetail.objects.filter(status=1, account=account).select_related('product')
        
        for order_detail in order_details:
            if order_detail.quantity > order_detail.product.qty:
                messages.error(request, f"Số lượng sản phẩm: {order_detail.product.name} không đủ trong kho. Chỉ còn {order_detail.product.qty} sản phẩm")
                check = False
        
        if check:
            with transaction.atomic():
                order = Order.objects.create(account=account, status=1)  # Thêm status vào Order mới
                for order_detail in order_details:
                    order_detail.status = 2
                    order_detail.order = order
                    order_detail.user = account
                    order_detail.selling_price = order_detail.product.selling_price * order_detail.quantity
                    order_detail.save()
                    order_detail.product.qty -= order_detail.quantity
                    order_detail.product.save()
                messages.success(request, "Đặt hàng thành công")
    
    return redirect('cart')

def get_best_selling(number_get):
    best_selling_products = Product.objects.annotate(total_buy=Count('orderdetail')).order_by('-total_buy')[:number_get]
    return best_selling_products

def get_latest_products(number_get):
    latest_products = Product.objects.order_by('-created_at')[:number_get]
    return latest_products

def update_order(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    account = request.user
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(account=account,status = 0)
    orderDetail, created = OrderDetail.objects.get_or_create(order=order,product = product)
    if action == 'add':
        orderDetail.quantity += 1
    elif action == 'remove':
        orderDetail.quantity -= 1
    orderDetail.save()
    if orderDetail.quantity <= 0:
        orderDetail.delete()
    return JsonResponse('added',safe=False)


