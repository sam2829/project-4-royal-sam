from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import *
from .forms import BookingFormDate, BookingFormTime

# This class is so the user can view the book a tee form


class BookATee(View):

    # Booking date form appears, user must select date and email
    def get(self, request, *args, **kwargs):
        
        
        return render(
            request,
            "book_a_tee.html",
            {
                "booking_form_date": BookingFormDate(),
            },
        )

    # User has selected date and posts form
    def post(self, request, *args, **kwargs):

        booking_form_date = BookingFormDate(data=request.POST)

        if booking_form_date.is_valid():
            booking_date = booking_form_date.save(commit=False)
            booking_date.user = request.user
            booking_date.save()
            return redirect('book_a_time')
        else:
            booking_form_date = BookingFormDate()

        return render(
            request,
            "book_a_tee.html",
            {
                "booking_form_date": BookingFormDate(),
            },
        )
    # this is so the user can view the booking time form

class BookATime(View):

    # Booking time form appears, user must select date and email
    def get(self, request, *args, **kwargs):

        return render(
            request,
            "book_a_time.html",
            {
                "booking_form_time": BookingFormTime(),
            },
        )
