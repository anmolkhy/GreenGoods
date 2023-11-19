# custom_filters.py

from django import template

register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    return int(value) * int(arg)
