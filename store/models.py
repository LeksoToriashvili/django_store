from enum import unique

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    stock = models.PositiveIntegerField(default=0, blank=False)
    image = models.ImageField(upload_to='products/', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
