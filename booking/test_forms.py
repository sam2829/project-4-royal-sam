from django.test import TestCase
from booking.forms import BookingFormDate, BookingFormTime


class TestBookingFormDate(TestCase):
    """
    Test for booking a date form
    """
    def test_valid_booking_form_date(self):
        # Test the BookingFormDate form is valid
        # with correct data.
        data = {'email': 'test@example.com', 'date': '2024-01-01'}
        form = BookingFormDate(data)
        # Check if valid
        self.assertTrue(form.is_valid())

    def test_invalid_booking_form_date_email(self):
        # Test the BookingFormDate form is invalid
        # with incorrect email.
        data = {'email': 'invalid-email', 'date': '2023-01-01'}
        form = BookingFormDate(data)
        # Check if invalid
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_invalid_booking_form_date_date(self):
        # Test the BookingFormDate form is invalid
        # with incorrect date.
        data = {'email': 'test@example.com', 'date': '2023-01-40'}
        form = BookingFormDate(data)
        # Check if invalid
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors)


class TestBookingFormTime(TestCase):
    """
    Test for booking a time form
    """
    def test_valid_booking_form_time(self):
        # Test the BookingFormTime form is valid
        # with correct data.
        data = {
            'time': '12:10',
            'number_of_players': 4,
            'member': True,
            'buggy': False
        }
        form = BookingFormTime(data, available_times=['12:10', '12:50'])
        # Check if valid
        self.assertTrue(form.is_valid())

    def test_invalid_booking_form_time_time(self):
        # Test the BookingFormTime form is invalid
        # with incorrect time.
        data = {
            'time': '12:00',
            'number_of_players': 4,
            'member': True,
            'buggy': False
        }
        form = BookingFormTime(data, available_times=['12:10', '12:50'])
        # Check if invalid
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors)

    def test_invalid_booking_form_time_players(self):
        # Test the BookingFormTime form is invalid
        # with incorrect number of players.
        invalid_players = ['5', '6', '7']
        for invalid_player in invalid_players:
            data = {
                'time': '12:10',
                'number_of_players': 7,
                'member': True,
                'buggy': False
            }
            form = BookingFormTime(data)
            # Check if invalid
            self.assertFalse(form.is_valid())
            self.assertIn('number_of_players', form.errors)
