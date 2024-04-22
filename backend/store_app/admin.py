from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','name', 'lastname', 'phone', 'created_at']

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['description', 'category', 'product_image', 'stock_quantity', 'price', 'created_at']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_image']    

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'unit_price', 'product_status', 'order_date']  

class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'total_amount', 'order_image']  

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'created_at']  


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)
admin.site.register(Favorite, FavoriteAdmin)