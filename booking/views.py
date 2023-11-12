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
        print(request.POST)

        if booking_form_date.is_valid():
            booking_date = booking_form_date.save(commit=False)
            booking_date.user = request.user
            selected_date = booking_form_date.cleaned_data['date']
            selected_date_str = selected_date.isoformat()
            request.session['date'] = selected_date_str
           
            return redirect('book_a_time')
        else:
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
       
        selected_date_str = request.session.get('date')

        if selected_date_str:
            selected_date = datetime.strptime(
                selected_date_str, '%Y-%m-%d').date()
            existing_times = Booking.objects.filter(
                date=selected_date).values_list('time', flat=True)
            # Replace YourModel and TIME_CHOICES with your actual model and choices
            available_times = [
                time[0] for time in AVAILABLE_TIMES if time[0] not in existing_times]
        else:
            available_times = [time[0] for time in AVAILABLE_TIMES]

        return render(
            request,
            "book_a_time.html",
            {
                "booking_form_time": BookingFormTime(available_times=available_times),
            },
        )
