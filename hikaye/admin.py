from django.contrib import admin
from .models import Story

# Register your models here.


class StoryAdmin(admin.ModelAdmin):
    list_display = ['title_or_parent','writer','score','is_reported']
    list_filter = ['is_reported']
    search_fields = ['title','content']
    fields = [
        ('title', 'parent'),
        'content',
        ('writer', 'is_reported'),
        ('creation_date', 'score')
    ]
    readonly_fields = ('creation_date', 'score')

admin.site.register(Story, StoryAdmin)
