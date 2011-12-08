from polls.models import Poll
from django.contrib import admin
from polls.models import Choice
from polls.models import Comment

class ChoiceInline(admin.TabularInline):
    model = Choice
    
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        (None,               {'fields': ['classification_top']}),
        (None,               {'fields': ['classification_low']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_today')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['comment']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('comment', 'pub_date', 'was_published_today')
    list_filter = ['pub_date']
    search_fields = ['comment']
    date_hierarchy = 'pub_date'


admin.site.register(Poll, PollAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Choice)

