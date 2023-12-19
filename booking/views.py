from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import *
from .forms import BookingFormDate, BookingFormTime
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date


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
            # Check if date selected hasnt already passed
            selected_date = booking_form_date.cleaned_data['date']
            if selected_date < date.today():
                messages.warning(request, 'Please select a future date.')
                return render(
                    request,
                    "book_a_tee.html",
                    {
                        "booking_form_date": booking_form_date,
                    },
                )
            
            booking_date = booking_form_date.save(commit=False)
            booking_date.user = request.user
            selected_date = booking_form_date.cleaned_data['date']
            selected_date_str = selected_date.isoformat()
            request.session['date'] = selected_date_str
            booking_email = request.POST.get('email')
            request.session['booking_email'] = booking_email

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

            # Filter out times that are in the past
            current_time = timezone.now().time()
            available_times = [
                time[0] for time in AVAILABLE_TIMES
                if time[0] not in existing_times and (
                    selected_date != timezone.now().date() or
                    datetime.combine(selected_date, datetime.strptime(time[0], '%H:%M').time(
                    )) > datetime.combine(timezone.now().date(), current_time)
                )
            ]

            # If there is no times available for for selected date user will be 
            # informed and redirected back to book a date form

            if not available_times:
                messages.warning(
                    request, 'No tee times available for the selected date. Please choose another date.')
                return HttpResponseRedirect(reverse('book_a_tee'))
        else:
            available_times = [
                time[0] for time in AVAILABLE_TIMES if (
                    selected_date != timezone.now().date() or
                    datetime.combine(selected_date, time[0]) > datetime.combine(
                        timezone.now().date(), current_time)
                )
            ]
        messages.info(request, f'You have selected the date: {selected_date}')
        return render(
            request,
            "book_a_time.html",
            {
                "booking_form_time": BookingFormTime(available_times=available_times),
            },
        )

    # User has selected time and posts form

    def post(self, request, *args, **kwargs):

        selected_date_str = request.session.get('date')

        if selected_date_str:
            selected_date = datetime.strptime(
                selected_date_str, '%Y-%m-%d').date()
            existing_times = Booking.objects.filter(
                date=selected_date).values_list('time', flat=True)
            available_times = [time[0]
                               for time in AVAILABLE_TIMES if time[0] not in existing_times]
        else:
            available_times = [time[0] for time in AVAILABLE_TIMES]

        booking_form_time = BookingFormTime(
            data=request.POST, available_times=available_times)

        if booking_form_time.is_valid():
            booking_time = booking_form_time.save(commit=False)
            booking_time.user = request.user
            booking_email = request.session.get('booking_email')
            booking_time.email = booking_email

            if selected_date_str:
                booking_time.date = selected_date

            booking_time.save()

            messages.success(request, f' You have successfully booked your tee '
                             f'time for: {booking_time.user}, {selected_date} '
                             f'at {booking_time.time} for {booking_time.number_of_players}.')
            return redirect('my_bookings')

        else:

            return render(
                request,
                "book_a_time.html",
                {
                    "booking_form_time": BookingFormTime(available_times=available_times),
                },
            )

# This class is so user can view there bookings


class MyBookings(LoginRequiredMixin, generic.ListView):

    model = Booking
    template_name = 'my_bookings.html'
    paginate_by = 3

    def get_queryset(self):

        # Get current date and time
        current_date = timezone.now().date()
        current_time = timezone.now().time()
        # Filter to show bookings for the user ordered by date and time
        # Filter also shows bookings that havnt passed
        bookings = Booking.objects.filter(
            user=self.request.user,
            date__gte=current_date,
        ).exclude(
            date=current_date,
            time__lte=current_time
        ).order_by('date', 'time')
        return bookings

        


        

# This class is for the user to edit a booking date

class EditBookingDate(View):

    # Gets the the form to edit date and displays the original data in form
    def get(self, request, item_id, *args, **kwargs):
        booking = get_object_or_404(Booking, id=item_id)
        booking_form_date = BookingFormDate(instance=booking)
        return render(
            request,
            "edit_tee_date.html",
            {
                "booking_form_date": booking_form_date,
            },
        )

    # User has selected date and posts form

    def post(self, request, item_id, *args, **kwargs):

        booking = get_object_or_404(Booking, id=item_id)
        booking_form_date = BookingFormDate(request.POST, instance=booking)

        if booking_form_date.is_valid():
            booking_date = booking_form_date.save(commit=False)
            booking_date.user = request.user
            selected_date = booking_form_date.cleaned_data['date']
            selected_date_str = selected_date.isoformat()
            request.session['date'] = selected_date_str
            booking_email = request.POST.get('email')
            request.session['booking_email'] = booking_email

            return redirect('edit_tee_time', item_id=booking.id)
        else:
            return render(
                request,
                "edit_tee_date.html",
                {
                    "booking_form_date": BookingFormDate(),
                },
            )

# This class is for user to edit booking time


class EditBookingTime(View):

    # Booking time form appears, user must select date and email
    def get(self, request, item_id, *args, **kwargs):

        selected_date_str = request.session.get('date')
        booking = get_object_or_404(Booking, id=item_id)
        booking_form_time = BookingFormTime(instance=booking)

        if selected_date_str:
            selected_date = datetime.strptime(
                selected_date_str, '%Y-%m-%d').date()
            existing_times = Booking.objects.filter(
                date=selected_date).values_list('time', flat=True)

            # Filter out times that are in the past
            current_time = timezone.now().time()
            available_times = [
                time[0] for time in AVAILABLE_TIMES
                if time[0] not in existing_times and (
                    selected_date != timezone.now().date() or
                    datetime.combine(selected_date, datetime.strptime(time[0], '%H:%M').time(
                    )) > datetime.combine(timezone.now().date(), current_time)
                )
            ]
        else:
            available_times = [
                time[0] for time in AVAILABLE_TIMES if (
                    selected_date != timezone.now().date() or
                    datetime.combine(selected_date, time[0]) > datetime.combine(
                        timezone.now().date(), current_time)
                )
            ]
        messages.info(request, f'You have selected the date: {selected_date}')
        return render(
            request,
            "edit_tee_time.html",
            {
                "booking_form_time": BookingFormTime(available_times=available_times),
            },
        )

    # User has selected time and posts form

    def post(self, request, item_id, *args, **kwargs):

        selected_date_str = request.session.get('date')
        booking = get_object_or_404(Booking, id=item_id)

        if selected_date_str:
            selected_date = datetime.strptime(
                selected_date_str, '%Y-%m-%d').date()
            existing_times = Booking.objects.filter(
                date=selected_date).values_list('time', flat=True)
            available_times = [time[0]
                               for time in AVAILABLE_TIMES if time[0] not in existing_times]
        else:
            current_time = timezone.now().time()
            available_times = [time[0] for time in AVAILABLE_TIMES if (
                selected_date != timezone.now().date() or
                datetime.combine(selected_date, time[0]) > datetime.combine(
                    timezone.now().date(), current_time)
            )]

        booking_form_time = BookingFormTime(
            data=request.POST, available_times=available_times, instance=booking)

        if booking_form_time.is_valid():
            booking_time = booking_form_time.save(commit=False)
            booking_time.user = request.user
            booking_email = request.session.get('booking_email')
            booking_time.email = booking_email

            if selected_date_str:
                booking_time.date = selected_date

            booking_time.save()

            messages.success(request, f' You have successfully booked your tee '
                             f'time for: {booking_time.user}, {selected_date} '
                             f'at {booking_time.time} for {booking_time.number_of_players}.')
            return redirect('my_bookings')

        else:
            return render(
                request,
                "edit_tee_time.html",
                {
                    "booking_form_time": booking_form_time,
                },
            )


# This class is for the user to confirm deletion a booking

class ConfirmDelete(View):

    def get(self, request, item_id):

        booking = get_object_or_404(Booking, id=item_id)
        return render(request, 'confirm_delete.html', {'booking': booking})

# This class is for the user to delete a booking

class DeleteBooking(View):

    def get(self, request, item_id):

        booking = get_object_or_404(Booking, id=item_id)
        booking.delete()
        return redirect('my_bookings')
        
