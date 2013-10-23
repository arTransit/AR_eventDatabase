from django.db import models
import calendar
import json

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=100)
    event_date = models.DateField()
    description = models.TextField()
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return "%s (%s) - %s" % (self.title,self.category,self.event_date)

    def to_JSON(self):
        return json.dumps( self.to_DICT) 
       
    def to_DICT(self):
        return ({ 
            'id': self.id, 
            'title':self.title,
            'event_date': calendar.timegm( self.event_date.timetuple() ),
            'description':self.description,
            'category':str(self.category) })
       


