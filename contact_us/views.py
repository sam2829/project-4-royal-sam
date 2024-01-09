from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.conf import settings
#from django.conf import settings


# This class it to render the gallery page

class ContactUs(TemplateView):

    #template_name = 'contact_us.html'

    #def get_context_data(self, **kwargs):

        #context = super().get_context_data(**kwargs)
        #context['GOOGLE_API_KEY'] = settings.GOOGLE_API_KEY
        #return context

    def my_forbidden_view(request):
        # Simulate a 403 Forbidden error
    raise PermissionDenied("Intentional 403 error for testing")
