from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.conf import settings


# This class it to render the gallery page

class ContactUs(TemplateView):

    """ This class is to render the Contact Us page """

    template_name = 'contact_us.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['GOOGLE_API_KEY'] = settings.GOOGLE_API_KEY
        return context
