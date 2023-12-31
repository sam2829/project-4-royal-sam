from .models import *
from django import forms

# This class is for the booking form to book a tee time
# and which fields I want to be shown


class BookingFormDate(forms.ModelForm):
   
    
    class Meta:
        model = Booking
        fields = ('email', 'date',)

        # Widget is used so the date is a calender option
        widgets = {

            'date': forms.DateInput(attrs={'type': 'date'})
        }


class BookingFormTime(forms.ModelForm):
    time = forms.ChoiceField(choices=AVAILABLE_TIMES)

    def __init__(self, *args, **kwargs):
        available_times = kwargs.pop('available_times', [])
        super().__init__(*args, **kwargs)
        self.fields['time'].choices = [(time, time)
                                       for time in available_times]


    
    class Meta:
        model = Booking
        fields = ('time', 'number_of_players', 'member', 'buggy',)