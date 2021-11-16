from django import template
from django.template.library import Library

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg