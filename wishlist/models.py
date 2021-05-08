from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class WishList(models.Model):
    """ Model for maintaining a wishlist """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.SET_NULL)
    added = models.DateTimeField(auto_now=True)


