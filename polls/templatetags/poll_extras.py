
from django import template

register=template.Library()

@register.simple_tag
def query_transform(request,**kwargs):

    updated=request.GET.copy()
    for k,v in kwargs.items():
        updated[k]=v
    return updated.urlencode()

@register.filter
def times(number):
    try:
        return range(int(number))
    except:
        return range(0)

@register.filter
def is_half(value):
    """
    Returns True if value ends with .5
    """
    try:
        return float(value) % 1 == 0.5
    except:
        return False