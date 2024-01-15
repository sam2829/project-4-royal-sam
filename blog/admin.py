from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    """
    This Class is to decide how the Post admin page
    lists, searches and functions.
    """

    list_display = ('title', 'slug', 'created_on', 'approved')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('approved', 'created_on')
    summernote_fields = ('content')
    actions = ['approve_posts']

    # This method is called to approve a post before it can be displayed

    def approve_posts(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    """
    This Class is to decide how the Post admin page
    lists, searches and functions.
    """

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    # This method is called to approve a comment before it can be displayed

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
