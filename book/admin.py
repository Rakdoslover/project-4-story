from django.contrib import admin
from .models import Chapter, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Chapter)
class ChapterAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('proposed_title', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('proposed_title', 'email', 'body')
