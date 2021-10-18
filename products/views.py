from django.shortcuts import render
from datetime import datetime
import os
import json
from .models import Product, ProductCategory

# Create your views here.
MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {
        'title': 'Geekshop',
        'date': datetime.now(),
    }
    return render(request, 'products/index.html', context)


def products(request):
    goods = Product.objects.all()
    context = {
        'title': 'Geekshop - Каталог',
        'products': goods
    }
    return render(request, 'products/products.html', context)
