from django.contrib import admin

from .models import News, NewsCategory
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display=('id','title','category','content','is_published')
    list_display_links=('id','title',)
    search_fields=('title','content')
    list_filter=('id','is_published',)
    list_editable=('is_published','category')
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')
    search_fields=('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)