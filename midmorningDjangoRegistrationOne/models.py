from django.db import models


#create a table called models
class Product(models.Model):
    prod_name = models.CharField(max_length=30, blank=False, null=False)
    prod_quantity = models.CharField(max_length=30, blank=False, null=False)
    prod_price = models.CharField(max_length=30, blank=False, null=False)

def __str__(self):
    return self.prod_name

#create a class called suppliers
class Supplier(models.Model):
    s_name = models.CharField(max_length=30, blank=False, null=False)
    s_email = models.CharField(max_length=30, blank=False, null=False)
    s_location = models.CharField(max_length=30, blank=False, null=False)
    s_product = models.CharField(max_length=30, blank=False, null=False)


def __str__(self):
    return self.s_name