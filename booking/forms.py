from .models import Booking
from django import forms

# This class is for the booking form to book a tee time
# and which fields I want to be shown


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('email', 'date', 'time', 'number_of_players', 'member',
                 'buggy',)


