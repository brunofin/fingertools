# -*- coding: UTF-8 -*-

from django.db import models
from fingertools.base.models import FTObject, Address

class Shop(FTObject):
    name = models.CharField(max_length = 255)
    icon = models.ImageField(upload_to='market/%Y%m%d')

class Affiliate(FTObject):
    icon = models.ImageField(upload_to='market/%Y%m%d')
    shop = models.ForeignKey(Shop, null = False)
    address = models.ForeignKey(Address, null = False)

class Category(models.Model):
    name = models.CharField(max_length = 25, null = False)
    description = models.CharField(max_length = 255, null = True)
    icon = models.ImageField(upload_to='market/%Y%m%d')

class Brand(FTObject):
    name = models.CharField(max_length = 70, null = False)
    icon = models.ImageField(upload_to='market/%Y%m%d')

class Product(FTObject):
    name = models.CharField(max_length = 70, null = False)
    price = models.FloatField(null = False)
    icon = models.ImageField(upload_to='market/%Y%m%d')
    brand = models.ForeignKey(Brand, null = False)
    category = models.ForeignKey(Category, null = False)
    affiliate = models.ManyToManyField(Affiliate, null = False)
    

