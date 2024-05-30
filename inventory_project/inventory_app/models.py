from django.db import models

class Product(models.Model):
    name: str  = models.CharField(max_length=100, null = False)
    category: str = models.CharField(max_length=100, null = False)
    price: float = models.FloatField(null = False)

    def __str__(self):
        return self.name
