from django.db import models

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


