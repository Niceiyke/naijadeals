# Generated by Django 4.2 on 2023-05-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_alter_product_discount_percent"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="stock",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
