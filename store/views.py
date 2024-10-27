from http.client import HTTPResponse
from itertools import product
from lib2to3.fixes.fix_input import context
from tkinter.font import names
from unicodedata import category

from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.template.context_processors import request

from store.models import Product, Category
from django.views.generic import DetailView, ListView


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product_list.html'
    paginate_by = 9

    def get_queryset(self):
        if self.kwargs.get('slug'):
            category = Category.objects.filter(slug=self.kwargs.get('slug')).first()
            return Product.objects.filter(category=category)
        else:
            return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(product_count=Count('products'))
        context['get_elided_page_range'] = context['paginator'].get_elided_page_range(self.request.GET.get(self.page_kwarg, 1))

        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = Product.objects.filter(category=self.object.category)
        return context
