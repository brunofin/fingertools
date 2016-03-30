# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

from fingertools.base.models import FTObject

class Image(FTObject):
	titulo = _('Image')
	image = models.ImageField(upload_to='img/%Y%m%d')
	description = models.CharField(max_length=255, null=True)
	
	def url(self):
		return '/v/' + str(self.id) + '/d'