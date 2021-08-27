from django.contrib import admin
from .models import  Desktops, Laptops, Order, OrderItem, Others, Phones

# admin.site.register(Category)
admin.site.register(Laptops)
admin.site.register(Others)
admin.site.register(Phones)
admin.site.register(Desktops)
admin.site.register(OrderItem)
admin.site.register(Order)

