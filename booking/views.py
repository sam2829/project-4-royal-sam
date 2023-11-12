from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import *
from .forms import BookingFormDate, BookingFormTime

# This class is so the user can view the book a tee form


class BookATee(View):

    def get(self, request, *args, **kwargs):
        
        
        return render(
            request,
            "book_a_tee.html",
            {
                "booking_form_date": BookingFormDate(),
            },
        )

    def post(self, request, *args, **kwargs):

        return render(
            request,
            "book_a_time.html",
            {
                "booking_form_time": BookingFormTime(),
            }
        )


    # this is so the user can post the booking a tee time form


    