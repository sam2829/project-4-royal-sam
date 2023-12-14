from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView


# This class it to render the gallery page

class ContactUs(TemplateView):

    template_name = 'contact_us.html'
