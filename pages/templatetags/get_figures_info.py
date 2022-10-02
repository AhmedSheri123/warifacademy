from django import template
from ..models import FiguresInfo

register = template.Library()

@register.simple_tag
def get_info(id):
    object = ""
    try:
        object = FiguresInfo.objects.get(figures__id=id).info
    except:
        pass
    return object