from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Product, Supplier



def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account saved successfully')
            return redirect('register')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

@login_required
def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def logout(request):
    return render(request, 'logout.html')

@login_required
def add_product(request):
    #check if form submitted has a method post
    if request.method == "POST":

        p_name = request.POST.get('jina')
        p_quantity = request.POST.get('kiasi')
        p_price = request.POST.get('bei')
        #finally save the data in our table called products
        product = Product(prod_name=p_name, prod_quantity=p_quantity,
                          prod_price=p_price)
        product.save()
        #Redirect back with a success message
        messages.success(request, 'Product saved successsfully')
        return redirect('add-product')
    return render(request, 'add_products.html')

@login_required
def view_products(request):
    #select the products to be displayed
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})

@login_required
def add_supplier(request):
    if request.method == "POST":
        s_name = request.POST.get('pedi')
        s_email = request.POST.get('mail')
        s_location = request.POST.get('pahali')
        s_product = request.POST.get('stuff')
        # finally save the data in our table called supplier
        supplier = Supplier(s_name=s_name, s_email=s_email, s_location=s_location,
                          s_product=s_product)
        supplier.save()
        # Redirect back with a success message
        messages.success(request, 'Supplier saved successsfully')
        return redirect('add_supplier')
    return render(request, 'add_suppliers.html')

@login_required
def delete_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('products')

@login_required
def update_product(request,id):
    product = Product.objects.get(id=id)
    #chekc if form submitted has ,method post
    if request.method == "POST":
        #recieve data from the form
        updated_name = request.POST.get('jina')
        updated_quantity = request.POST.get('kiasi')
        updated_price = request.POST.get('bei')
        #update product with recieved updated data
        product.prod_name = updated_name
        product.prod_quantity =updated_quantity
        product.prod_price = updated_price

        #Return data to database and redirect back
        #to products page with a success message
        product.save()
        messages.success(request, 'Product updated successfully')
        return redirect('products')
    return render(request, 'update_product.html', {'product':product})

@login_required
def payment(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'payment.html', {'product' : product})