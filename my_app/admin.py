from django.contrib import admin
from .models import Product, Firm, Category
# Register your models here.
admin.site.register(Product)
admin.site.register(Firm)
admin.site.register(Category)
