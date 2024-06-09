from django import template
from news.models import NewsCategory

register = template.Library()

@register.simple_tag(name='get_cats')
def get_cats():
    return NewsCategory.objects.all()

@register.inclusion_tag('news/listcat.html')
def listcats():
    cats = NewsCategory.objects.all()
    return {'cats': cats}