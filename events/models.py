from django.db import models
import datetime

class Event(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.name

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()

    def pub_date_ft(self):
        return self.pub_date.strftime("%A, %d. %B %Y ")
