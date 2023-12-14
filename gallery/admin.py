from django.contrib import admin
from .models import GalleryImage
from django_summernote.admin import SummernoteModelAdmin


@admin.register(GalleryImage)
class GalleryImageAdmin(SummernoteModelAdmin):

    list_display = ('image', 'caption')
    search_fields = ['caption']