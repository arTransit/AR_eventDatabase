from django.db import models
from django.contrib import admin

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title',)
    
class Event(models.Model):
    title = models.CharField(max_length=100)
    event_date = models.DateField()
    description = models.TextField()
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return "%s (%s) - %s" % (self.title,self.category,self.event_date)

class EventAdmin(admin.ModelAdmin):
    list_display = ['title','category','event_date','description']
    ordering = ['-event_date','title']

admin.site.register(Event,EventAdmin)
admin.site.register(Category, CategoryAdmin)


