from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Product, UserProduct




# Create your views here.
def homepage(request):
    return render(request, 'app/homepage.html')

def registration_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # You can add more validation and error handling here.

        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        # Log in the user immediately after registration
        login(request, user)
        return redirect('user_dashboard')  # Redirect to the user_dashboard after registration

    return render(request, 'app/registration.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Use the authenticate function to verify user credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # The user is valid, log them in
            login(request, user)
            return redirect('user_dashboard')  # Redirect to the user dashboard
    
    return render(request, 'app/login.html')


@login_required(login_url='/login/')
def user_dashboard(request):
    # Get all UserProduct instances associated with the logged-in user
    user_products = Product.objects.filter(userproduct__user=request.user)

    # Get products that are with the collector
    products_with_collector = Product.objects.filter(with_collector=True)
    
    return render(request, 'app/user_dashboard.html', {'user_products': user_products, 'products_with_collector': products_with_collector,})

def user_logout(request):
    logout(request)
    return redirect('homepage')

def view_products(request):
    products = Product.objects.filter(is_available=True)  # Retrieve all available products
    
    # Get products that the user has purchased
    user_purchased_products = UserProduct.objects.filter(user=request.user).values_list('product', flat=True)
    
    # Exclude purchased products from the available products
    products = products.exclude(id__in=user_purchased_products)
    
    return render(request, 'app/view_products.html', {'products': products})

@login_required
def buy_product(request, product_id):
    
    product = get_object_or_404(Product, pk=product_id)
    
    # Check if the product is available
    if not product.is_available:
        messages.error(request, "This product is no longer available.")
        return redirect('view_products')
    
    # Create a UserProduct instance to associate the user with the product
    user_product = UserProduct(user=request.user, product=product)
    user_product.save()
    
    # Mark the product as unavailable
    product.is_available = False
    product.save()
    
    messages.success(request, "You have successfully purchased the product.")
    return redirect('view_products')

def give_to_collector(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if not product.with_collector:
        # Move the product to the collector
        product.with_collector = True
        product.save()

        # Remove the product from the user dashboard
        user_product = UserProduct.objects.get(user=request.user, product=product)
        user_product.delete()

        messages.success(request, "Product has been given to the collector.")
    else:
        messages.error(request, "Product is already with the collector.")

    return redirect('user_dashboard')

def track_products_with_collector(request):
    # Retrieve products that are with the collector
    products_with_collector = Product.objects.filter(with_collector=True)
    
    return render(request, 'app/user_dashboard.html', {'products_with_collector': products_with_collector})

def return_product_to_available(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if product.with_collector:
        # Remove the association with the collector
        product.with_collector = False
        product.save()

        # Check if the user had purchased this product
        try:
            user_product = UserProduct.objects.get(user=request.user, product=product)
            user_product.delete()  # Remove the association with the user
        except UserProduct.DoesNotExist:
            pass  # If the user didn't purchase this product, do nothing

        # Mark the product as available again
        product.is_available = True
        product.save()

        messages.success(request, "Product has been returned to the available list.")
        return redirect('track_products_with_collector')
    else:
        messages.error(request, "Product is not with the collector.")
        return redirect('track_products_with_collector')