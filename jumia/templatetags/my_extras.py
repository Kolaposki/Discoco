"""
    name='my_extras',
    project='stellar'
    date='12/30/2019',
    author='Oshodi Kolapo',
"""

from django import template

register = template.Library()


@register.filter(name='shortner')
def shortner(product):
    if len(product) > 80:
        return product[0:83] + '...'
    else:
        return product


@register.filter(name='toint')
def toint(product):
    return int(product)
