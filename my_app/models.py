from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    firm = models.CharField(max_length=50)
    category = models.CharField(max_length=50)


class Firm(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)
