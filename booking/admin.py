from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """
    This class is so the admin page is displayed and functioned.
    """

    list_display = ('user', 'email', 'date', 'time',
                    'number_of_players', 'member', 'buggy')
    search_fields = ('user__username', 'email', 'date', 'time')
    list_filter = ('date', 'time')
    summernote_fields = ('content')
