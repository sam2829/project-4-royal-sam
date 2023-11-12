from .models import *
from django import forms

# This class is for the booking form to book a tee time
# and which fields I want to be shown


class BookingFormDate(forms.ModelForm):
    
    
    class Meta:
        model = Booking
        fields = ('email', 'date',)


class BookingFormTime(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('time', 'number_of_players', 'member', 'buggy',)