from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView


# This class it to render the gallery page

class Gallery(TemplateView):

    template_name = 'gallery.html'
