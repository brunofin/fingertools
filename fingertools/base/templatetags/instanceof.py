from django import template
from django.utils.importlib import import_module


register = template.Library()

@register.filter
def instanceof(value, class_str):
    print value
    split = class_str.split('.')
    return isinstance(value, getattr(import_module('.'.join(split[:-1])), split[-1]))