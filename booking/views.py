from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm

# This class is so the user can view the book a tee form


class BookATee(View):

    def get(self, request):

        return render(request, 'book_a_tee.html',
        {
            "booking_form": BookingForm(),
        })


    # this is so the user can [ost the booking a tee time form

    
    def post(self, request):

        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
        else:
            booking_form = BookingForm()

        return render(
            request,
            "book_a_tee.html",
            {
                "booking_form": BookingForm(),
            },
        )
