from webapp.models import Product
from webapp.forms import ProductForm, FindForm
from django.shortcuts import render, get_object_or_404, redirect

def index_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = FindForm()
        products = Product.objects.exclude(amount=0).order_by('category', 'name')
        categories = []
        for product in products:
            print(str(product.category))
            category = str(product.category)
            # print(category[1].strip())
            if category not in categories:
                categories.append(category)
        return render(request, 'index.html', context={'products': products, 'form': form, 'categories': categories})
    elif request.method =='POST':
        prod_del = request.POST.getlist('del')
        Product.objects.filter(pk__in=prod_del).delete()
        return redirect('index')

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', context={'product': product})

def product_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_create.html', context={'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task = Product.objects.create(name=data['name'], description=data['description'], category=data['category'],
                                          amount=data['amount'], price=data['price'])
            return redirect('product_view', pk=task.pk)
        else:
            return render(request, 'product_create.html', context={'form': form})

def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(data={'name': product.name, 'description': product.description, 'category': product.category, 'amount': product.amount, 'price': product.price})
        return render(request, 'product_update.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.category = request.POST.get('category')
        product.amount = request.POST.get('amount')
        product.price = request.POST.get('price')

        product.save()
        return redirect('product_view', pk=product.pk)

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'product_delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index')

def find_view(request, *args, **kwargs):
    form =FindForm(data=request.GET)
    if form.is_valid():
        name = form.cleaned_data['name']
        products = Product.objects.filter(name__contains=name).exclude(amount=0).order_by('category', 'name')
        return render(request, 'index.html', {'products': products, 'form': form})
    else:
        return redirect('index')