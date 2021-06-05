from django.contrib import admin
from .models import Product, Product_type


class ProductAdmin(admin.ModelAdmin):
    """ This class has been copied
    and adapted from the Boutique Ado Project """
    list_display = (
        'name',
        'display_name',
        'colour',
        'description',
        'quantity_in_pack',
        'image',
    )


class Product_typeAdmin(admin.ModelAdmin):
    """ This class has been copied and
    adapted from the Boutique Ado Project """
    list_display = (
        'display_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Product_type, Product_typeAdmin)


