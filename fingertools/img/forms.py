# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from fingertools.img.models import Image
from fingertools.base.forms import FTForm


class FormImage(FTForm):
	image = forms.ImageField(label=_(u'Image'), required=True)
	description = forms.CharField(label=_(u'Description'), required=False)
	
	class Meta:
		model = Image
		fields = ('image', 'description')
