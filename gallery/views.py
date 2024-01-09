from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import GalleryImage


# This class it to render the gallery page

class Gallery(TemplateView):

    #def get(self, request, *args, **kwargs):

        #images = GalleryImage.objects.all()
        #return render(request, 'gallery.html', {'images': images})
    def my_error_view(request):
        # Simulate an error by raising an exception
    raise Exception("Intentional error for testing 500 page")
