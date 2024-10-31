"""
URL configuration for django_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from itertools import product

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from store import views

import store
from store.views import ProductListView, ProductDetailView
from order.views import CartListView, AddToCartView, CheckoutView
from core.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_details'),
    path('category/', ProductListView.as_view(), name='product_list'),
    path('category/<slug:slug>/', ProductListView.as_view(), name='product_list'),
    path('cart/', CartListView.as_view(), name='cart_list'),
    path('add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('register/', RegisterView.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
