from .models import *
from django import forms


# This class is for the booking date form to book a tee date
# and which fields I want to be shown

class BookingFormDate(forms.ModelForm):
    """
    This class is for the booking date form.
    """

    class Meta:
        model = Booking
        fields = ('email', 'date',)

        # Widget is used so the date is a calender option
        widgets = {

            'date': forms.DateInput(attrs={'type': 'date'})
        }

# This class is for the booking tee time form to book a tee time
# and which fields I want to be shown


class BookingFormTime(forms.ModelForm):
    """
    This class is for the booking time form.
    """
    time = forms.ChoiceField(choices=AVAILABLE_TIMES)

    def __init__(self, *args, **kwargs):
        available_times = kwargs.pop('available_times', [])
        super().__init__(*args, **kwargs)
        self.fields['time'].choices = [(time, time)
                                       for time in available_times]

    def clean(self):
        cleaned_data = super().clean()
        selected_time = cleaned_data.get('time')
        selected_date = cleaned_data.get('date')

        if selected_time and selected_date:
            existing_times = Booking.objects.filter(
                date=selected_date, time=selected_time)

            if existing_times.exists():
                raise ValidationError(
                    'The selected time has been booked by another user. '
                    'Please choose another time.')
                print("validation error raised")

    class Meta:
        model = Booking
        fields = ('time', 'number_of_players', 'member', 'buggy',)
