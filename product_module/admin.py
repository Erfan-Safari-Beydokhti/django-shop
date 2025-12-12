from django.contrib import admin

from product_module.models import Product, ProductCategory, ProductVisit, ProductTag, ProductGallery, ProductBrand, \
     ProductReview

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductVisit)
admin.site.register(ProductTag)
admin.site.register(ProductGallery)
admin.site.register(ProductBrand)
admin.site.register(ProductReview)
