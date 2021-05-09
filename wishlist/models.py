from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class WishList(models.Model):
    """ Model for maintaining a wishlist """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(
        Product,
        through="WishListItem",
        null=True,
        blank=True,
        related_name="product_wishlists")
    added = models.DateTimeField(auto_now=True)


class WishListItem(models.Model):
    """
    This is the 'through' model, which is the link between products
    and wishlists. Each item on the wishlist is FK'd to both a product
    and its respective wishlist through this model.

    With this change, you should be able to add as many products to a
    wishlist as you want, and each product can be on as many wishlists
    as you want. Django will automatically create these WishListItems
    as you add products to wishlists.

    You can access the products on each wishlist with
    my_wishlist.products.all() or you can access the wishlists that a
    product is on with my_product.product_wishlists.all() (note the
    related_name on the M2M field)
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
