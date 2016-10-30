from django.db import models


class Product(models.Model):
    product_id = models.CharField(max_length=30, primary_key=True)
    product_name = models.CharField(max_length=100)
    large_category = models.CharField(max_length=30)
    medium_category = models.CharField(max_length=30)
    small_category = models.CharField(max_length=30)
    production_company = models.CharField(max_length=30)
    product_line = models.CharField(max_length=30)
    retail_price = models.IntegerField()
    inbound_price = models.IntegerField()
