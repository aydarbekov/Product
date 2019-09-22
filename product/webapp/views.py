from webapp.models import Product
from django.shortcuts import render, get_object_or_404, redirect

def index_view(request, *args, **kwargs):
    if request.method == 'GET':
        products = Product.objects.exclude(amount=0).order_by('category', 'name')
        return render(request, 'index.html', context={'products': products})

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', context={'product': product})






