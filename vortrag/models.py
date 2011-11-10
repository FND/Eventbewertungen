from django.db import models
import datetime
from events.models import Event

# Create your models here.

class Vortrag(models.Model):
    event = models.ForeignKey(Event)
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.name

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
