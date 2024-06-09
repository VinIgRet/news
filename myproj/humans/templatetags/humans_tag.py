from django import template
from humans.models import Professions

register = template.Library()

@register.simple_tag(name='get_profs')
def get_profs():
    return Professions.objects.all()

@register.inclusion_tag('humans/listprofs.html')
def listcats():
    profs = Professions.objects.all()
    return {'profs': profs}