from django.shortcuts import get_object_or_404, render, redirect

from .forms import ProductForm, ClientForm
from .models import Product, Client

def home(request):
    return render(request, 'home/index.html')


# Products Start
def products(request):
    products = Product.objects.all()

    print(products)
    return render(request, "products/index.html", {"products": products})
    
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products') 
    else:
        form = ProductForm()

    
    return render(request, 'products/add_product.html', {'form': form})

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')  # إعادة توجيه إلى صفحة قائمة المنتجات
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'form': form, 'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('products')  
# Products End

# Clients Start 

def clients(request):
    clients = Client.objects.all()

    return render(request, "products/index.html", {"clients": clients})
    
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients') 
    else:
        form = ClientForm()

    
    return render(request, 'client/add_client.html', {'form': form})

def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client') 
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/edit_client.html', {'form': form, 'client': client})

def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return redirect('clients')  

# Clients End