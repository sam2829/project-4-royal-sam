from .models import *
from django import forms


# This class is for the booking date form to book a tee date
# and which fields I want to be shown

class BookingFormDate(forms.ModelForm):
    """
    This class is for booking a date form.
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
    This class is for booking a time form.
    """
    time = forms.ChoiceField(choices=AVAILABLE_TIMES)

    def __init__(self, *args, **kwargs):
        available_times = kwargs.pop('available_times', [])
        super().__init__(*args, **kwargs)
        self.fields['time'].choices = [(time, time)
                                       for time in available_times]

    class Meta:
        model = Booking
        fields = ('time', 'number_of_players', 'member', 'buggy',)
