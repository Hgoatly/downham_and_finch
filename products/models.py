from django.db import models


class Product_type(models.Model):
    """ This model has been copied and
    adapted from the Boutique Ado project """
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    """ This model has been copied and
    adapted from the Boutique Ado project """
    product_type = models.ForeignKey(
        'Product_type', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)
    colour = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    quantity_in_pack = models.DecimalField(
        max_digits=2, decimal_places=0, null=True, blank=True)
    quantity_in_stock = models.DecimalField(
        max_digits=2, decimal_places=0, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    display_product = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Custom(models.Model):
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=254, null=True, blank=True)
    has_fabric_choice = models.BooleanField(default=False, null=True, blank=True)
    has_nose_wire = models.BooleanField(default=False, null=True, blank=True)
    description = models.TextField()
    size = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class FabricChoice(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


