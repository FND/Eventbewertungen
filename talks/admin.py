from django.contrib import admin
from talks.models import Talk
from polls.models import Poll
import datetime

class PollInline(admin.TabularInline):
    model = Poll

class TalkAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [PollInline]
    list_display = ('name', 'pub_date', 'was_published_today')
    list_filter = ['pub_date']
    search_fields = ['name']
    date_hierarchy = 'pub_date'

    def save_model(self, request, obj, form, change):
        poll = Poll.objects.create(question="Das Thema war:", pub_date=datetime.datetime.now())
        Talk.objects.add(poll)
        Talk.save()

admin.site.register(Talk, TalkAdmin)


