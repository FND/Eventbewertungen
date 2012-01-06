from django.contrib import admin
from events.models import Event
from talks.models import Talk


class TalkInline(admin.TabularInline):
    model = Talk


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [TalkInline]
    list_display = ('name', 'pub_date', 'was_published_today')
    list_filter = ['pub_date']
    search_fields = ['name']
    date_hierarchy = 'pub_date'

    class Media:
        css = {
        'all': ('base.css',),
        }

admin.site.register(Event, EventAdmin)
