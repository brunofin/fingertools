# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from fingertools.base.models import FTObject

class FTForm(forms.ModelForm):
    tags = forms.CharField(label=_(u'Tags'), required = False)
    
    class Meta:
        model = FTObject