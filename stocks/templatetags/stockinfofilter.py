from django import template

register = template.Library()

@register.filter
def get(mapping, key):
    return mapping.get(key, '')

@register.filter
def removedot(id):
    return id.replace('.', '')

@register.filter
def getchange(mapping):
    change = mapping.get('Quote Price') - mapping.get('Previous Close')
    return change