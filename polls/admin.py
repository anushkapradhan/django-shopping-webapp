from django.contrib import admin
# from .models import  ganpatiProducts, diwaliProducts, christmasProducts
from .models import siteProducts, MyCart, MyOrder

# Register your models here.

# admin.site.register(ganpatiProducts)

# admin.site.register(diwaliProducts)

# admin.site.register(christmasProducts)

admin.site.register(siteProducts)

admin.site.register(MyCart)

admin.site.register(MyOrder)