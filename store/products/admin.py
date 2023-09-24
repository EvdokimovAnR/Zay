from django.contrib import admin
from products.models import ProductCategory, Product, Basket, ProductInfo

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Basket)
admin.site.register(ProductInfo)


