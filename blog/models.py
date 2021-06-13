from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=254)
    content = models.TextField(max_length=800)
    image = models.ImageField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
