from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=1000, primary_key=True)
    discount_price = models.PositiveIntegerField()
    original_price = models.PositiveIntegerField()
    image = models.URLField()
    product_url = models.URLField()
    discount_percent = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)
    store = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-discount_percent"]
