from django.contrib import admin
from .models import Order, CartItem, Item
# Register your models here.

admin.site.register(Order)
admin.site.register(CartItem)
admin.site.register(Item)