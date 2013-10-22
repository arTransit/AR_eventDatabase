from django.contrib import admin
from eventdb.models import Event,Category

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title',)
    
class EventAdmin(admin.ModelAdmin):
    list_display = ['title','category','event_date','description']
    ordering = ['-event_date','title']

admin.site.register(Event,EventAdmin)
admin.site.register(Category, CategoryAdmin)
