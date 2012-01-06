from django.contrib import admin
from talks.models import Talk
from polls.models import Poll
from polls.models import Comment
import datetime


class PollInline(admin.TabularInline):
    model = Poll


class CommentInline(admin.TabularInline):
    model = Comment


class TalkAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [PollInline,
               CommentInline]
    list_display = ('name', 'pub_date', 'was_published_today')
    list_filter = ['pub_date']
    search_fields = ['name']
    date_hierarchy = 'pub_date'

admin.site.register(Talk, TalkAdmin)
