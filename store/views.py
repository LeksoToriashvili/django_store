from http.client import HTTPResponse
from tkinter.font import names

from django.http import JsonResponse
from django.shortcuts import render

from store.models import Product, Category


def product_details(request, slug):
    if not slug:
        return render(request, 'base.html')
    product = Product.objects.get(slug=slug)
    category = Category.objects.get(id=product.category.id)
    related_products = Product.objects.filter(category=category)
    return render(request, 'product_details.html', {'product': product, 'related_products': related_products})


def product_list(request, slug=None):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product_list.html', {'products': products, 'categories': categories})
