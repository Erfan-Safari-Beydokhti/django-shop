
from django import template
from django.utils import timezone

register=template.Library()

@register.simple_tag
def query_transform(request,**kwargs):

    updated=request.GET.copy()
    for k,v in kwargs.items():
        updated[k]=v
    return updated.urlencode()

@register.filter(name='show_datetime')
def show_datetime(value):
    local_time= timezone.localtime(value)
    return local_time.strftime('%Y-%m-%d')