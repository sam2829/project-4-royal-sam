from django.test import TestCase
from .models import Booking
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


class TestBookingModel(TestCase):
    """
    Test booking model
    """
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_booking_creation(self):
        # Create a booking
        booking = Booking.objects.create(
            user=self.user,
            email='test@example.com',
            date=datetime.now(),
            time='07:30',
            number_of_players='2',
            member=True,
            buggy=False
        )
        # Check booking was created
        self.assertEqual(Booking.objects.count(), 1)

        # Check the data in model is what was provided
        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.email, 'test@example.com')
        self.assertEqual(booking.time, '07:30')
        self.assertEqual(booking.number_of_players, '2')
        self.assertEqual(booking.member, True)
        self.assertEqual(booking.buggy, False)

    def test_booking_defaults(self):
        # Check that the booking has default vales.
        booking = Booking.objects.create(
            user=self.user,
            email='test@example.com',
        )
        # Check the default values
        self.assertEqual(booking.time, '07:30')
        self.assertEqual(booking.number_of_players, '1')
        self.assertEqual(booking.member, False)
        self.assertEqual(booking.buggy, False)
