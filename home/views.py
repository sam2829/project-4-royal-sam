from django.shortcuts import render
from django.views import generic, View
from django.views.generic import TemplateView
from django.http import HttpResponseNotFound


# This class it to render the homepage

class HomeView(TemplateView):
    """
    This class is to render the homepage.
    """

    template_name = 'index.html'
