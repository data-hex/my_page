from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@stringfilter
@register.filter(name='split')
def split(value, key=" "):
    return value.split(key)

@register.filter(name='times')
def times(value):
    return range(value)

@register.filter(name='filter_range')
def filter_range(start, end):
    return range(start, end)