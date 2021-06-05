from django.db import models


class Blog(models.Model):
    """ This model has been copied and
    adapted from the Boutique Ado project """
    title = models.CharField(max_length=254)
    content = models.Textfield()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
