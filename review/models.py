from django.db import models


class Review(models.Model):
    name = models.CharField(
        max_length=200)
    review = models.TextField(max_length=800)

    def __str__(self):
        return self.name
