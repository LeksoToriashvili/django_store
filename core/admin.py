from django.contrib import admin
from .models import CustomUserModel


@admin.register(CustomUserModel)
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'last_active_datetime', 'is_superuser', 'is_staff')
