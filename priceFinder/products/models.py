from django.db import models

# Create your models here.

class Product(models.Model):
    name =models.CharField(max_length=300)
    discount_price =models.PositiveIntegerField()
    original_price =models.PositiveIntegerField()
    image=models.URLField()

    def __str__(self):
        return self.name

