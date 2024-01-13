from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import GalleryImage


# This class it to render the gallery page

class Gallery(TemplateView):
    """
    This class is to render the gallery page
    """

    def get(self, request, *args, **kwargs):

        images = GalleryImage.objects.all()
        return render(request, 'gallery.html', {'images': images})
