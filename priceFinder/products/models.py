from django.db import models

# Create your models here.

class Product(models.Model):
    name =models.CharField(max_length=300)
    discount_price =models.PositiveIntegerField()
    original_price =models.PositiveIntegerField()
    image=models.URLField()
    product_url=models.URLField()
    discount_percent=models.CharField(max_length=4)
    category=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        ordering =['-discount_percent']

