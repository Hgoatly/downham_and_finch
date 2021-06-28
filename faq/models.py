from django.db import models
from django.utils import timezone


class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(max_length=800)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question
