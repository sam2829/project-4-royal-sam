from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html


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

    list_display = (
        'name',
        'get_short_body',
        'get_short_post',
        'created_on',
        'approved'
    )
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    # This method is called to approve a comment before it can be displayed

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    # This method returns a shortened version of the comment body
    # for the list view
    def get_short_body(self, obj):
        return format_html(
            f'{obj.body[:100]}...'
        ) if len(obj.body) > 100 else obj.body

    get_short_body.short_description = 'Comment Body'

    # This method returns a shortened version of the comment post
    # for the list view
    def get_short_post(self, obj):
        post_text = str(obj.post) if obj.post else ''
        return format_html(
            f'{post_text[:100]}...'
        ) if len(post_text) > 100 else post_text

    get_short_post.short_description = 'Comment Post'
