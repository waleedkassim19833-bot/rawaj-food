from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    return render(request, 'products/home.html', {
        'products': products,
        'categories': categories,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {
        'product': product,
    })