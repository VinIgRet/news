from django.contrib import admin

from .models import Humans, Professions

# Register your models here.

class HumansAdmin(admin.ModelAdmin):
    list_display=('id','nicname','famil','name','otches','profession','birthday','ismale')
    list_display_links=('id','nicname')
    search_fields=('nicname','famil','name')
    list_filter=('id','profession','ismale')
    list_editable=('ismale','profession')
class ProfessionsAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')
    search_fields=('title',)
    
admin.site.register(Humans, HumansAdmin)
admin.site.register(Professions, ProfessionsAdmin)