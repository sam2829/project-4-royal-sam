from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView


# This class it to render the homepage

class HomeView(TemplateView):

    template_name = 'index.html'
