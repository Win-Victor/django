from django.shortcuts import render
from datetime import datetime
import os
import json
from .models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {
        'title': 'Geekshop',
        'date': datetime.now(),
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {'title': 'Geekshop - Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    context['products'] = products
    return render(request, 'products/products.html', context)
