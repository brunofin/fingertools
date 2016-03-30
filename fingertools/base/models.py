# -*- coding: UTF-8 -*-

from django.contrib.auth.models import User
from django.db import models
from fingertools.base import choices


class Tag(models.Model):
    tag = models.CharField(max_length=50, null=False, unique=True)

class FTObject(models.Model):
    uploader_ip = models.IPAddressField()
    date = models.DateField()
    time = models.TimeField()
    views = models.PositiveIntegerField()
    user = models.ForeignKey(User, null=True)
    tags = models.ManyToManyField(Tag, null=True)
    
class Referer(models.Model):
    """
    request.META.HTTP_REFERER
    """
    referer_url = models.URLField(null = False)
    object = models.ForeignKey(FTObject, null=False)

class LatLon(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

class Address(models.Model):
    logradouro = models.CharField(max_length = 255, null = False)
    numero = models.CharField(max_length = 10, null = False)
    bairro = models.CharField(max_length = 100, null = False)
    CEP = models.CharField(max_length = 8, null = False)
    cidade = models.CharField(max_length = 50, null = False)
    estado = models.CharField(max_length = 2, null = False, choices = choices.UF.list)
    latlon = models.ForeignKey(LatLon, null = True)
