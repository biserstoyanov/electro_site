# Create your models here.
from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="services/", blank=True, null=True)

    def __str__(self):
        return self.title
