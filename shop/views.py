from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ProductForm
from .models import Product

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Registration successful")
        return redirect('login')

    return render(request, 'register.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            next_url = request.GET.get('next')
            return redirect(next_url or 'dashboard')

        messages.error(request, "Invalid username or password")
        return redirect('login')

    return render(request, 'login.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

def logout_user(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url='login')
def products(request):
    product_list = Product.objects.all()
    return render(request, 'products.html', {'products': product_list})

@login_required(login_url='login')
def add_products(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product saved successfully.")
            return redirect('products')
        messages.error(request, "Please correct the errors below.")
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})
