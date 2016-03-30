# -*- coding: utf-8 -*-

from django import forms

from django.utils.translation import ugettext_lazy as _
from fingertools.text.models import Texto
from fingertools.base.forms import FTForm

class FormTexto(FTForm):
	text = forms.CharField(label=_(u'Source code'), required=True, widget=forms.Textarea)
	language = forms.ChoiceField(label=_(u'Language'), required=True, choices=Texto.LANGUAGE_CHOICES)
	titulo = forms.CharField(label=_(u'Title'), required=False)
	expires = forms.ChoiceField(label=_(u'Expiration'), required=True, choices=Texto.EXPIRES_CHOICES)
	exposure = forms.ChoiceField(label=_(u'Exposure'), required=True, choices=Texto.EXPOSURE_CHOICES)
	
	class Meta:
		model = Texto
		fields = ('text', 'language', 'titulo', 'expires', 'exposure')
