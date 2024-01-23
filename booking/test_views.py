from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .models import Booking
from django.contrib.auth import get_user_model
from django.utils import timezone


class TestBookingViews(TestCase):
    """
    Test for booking views
    """
    def setUp(self):
        # Create a user for testing
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_book_a_tee_get(self):
        # Check the book a tee page renders correctly
        response = self.client.get(reverse('book_a_tee'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_a_tee.html')

    def test_book_a_tee_post_valid(self):
        # Test the POST request for the 'book_a_tee' view with
        # the correct data in this case one day from the present day
        data = {
            'date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'),
            'email': 'test@example.com',
        }

        # Simulate a logged-in user
        self.client.force_login(self.user)
        # If valid reidrects to book a time page
        response = self.client.post(reverse('book_a_tee'), data)
        self.assertRedirects(response, reverse('book_a_time'))

    def test_book_a_tee_post_invalid_date(self):
        # Test the POST request for the 'book_a_tee' view with
        # the incorrect data for date
        data = {
            'date': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
            'email': 'test@example.com',
        }

        # If invalid reverse back to book a tee page
        response = self.client.post(reverse('book_a_tee'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_a_tee.html')

    def test_book_a_tee_post_invalid_email(self):
        # Test the POST request for the 'book_a_tee' view with
        # the incorrect data for email
        data = {
            'date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'),
            'email': 'invalid email',
        }

        # If invalid reverse back to book a tee page
        response = self.client.post(reverse('book_a_tee'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_a_tee.html')

    def test_confirm_delete_get(self):
        # Test confirm delete view
        # Create a booking
        booking = Booking.objects.create(
            user=self.user,
            email='test@example.com',
            date=datetime.now().date(),
            time='07:30',
            number_of_players='2',
            member=True,
            buggy=False
        )
        # Simulate a logged-in user
        self.client.force_login(self.user)
        response = self.client.get(reverse('confirm_delete', args=[booking.id]))
        # Check that user is being taken to the delete page
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirm_delete.html')

    def test_confirm_delete_get_unauthorized(self):
        # Test confirm delete view if unauthorized
        # Create a booking
        booking = Booking.objects.create(
            user=self.user,
            email='test@example.com',
            date=datetime.now().date(),
            time='07:30',
            number_of_players='2',
            member=True,
            buggy=False
        )
        # Simulate a user who is not the owner of the booking
        other_user = User.objects.create_user(
            username='otheruser',
            password='otherpassword'
        )
        self.client.force_login(other_user)
        response = self.client.get(reverse('confirm_delete', args=[booking.id]))
        # Check that user is being taken to 403 Forbidden page
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, '403.html')

    def test_delete_booking(self):
        # Test the 'delete_booking' view
        # Create booking
        booking = Booking.objects.create(
            user=self.user,
            email='test@example.com',
            date=datetime.now().date(),
            time='07:30',
            number_of_players='2',
            member=True,
            buggy=False
        )
        # Simulate a logged-in user
        self.client.force_login(self.user)
        response = self.client.get(reverse('delete_booking', args=[booking.id]))
        # Check that user is redirected to my bookings after delete
        self.assertRedirects(response, reverse('my_bookings'))

    def test_delete_booking_unauthorized(self):
        # Test 'delete_booking' view if unauthorizes
        # Create a booking
        booking = Booking.objects.create(
            user=self.user,
            email='test@example.com',
            date=datetime.now().date(),
            time='07:30',
            number_of_players='2',
            member=True,
            buggy=False
        )
        # Simulate a user who is not the owner of the booking
        other_user = User.objects.create_user(
            username='otheruser',
            password='otherpassword'
        )
        self.client.force_login(other_user)
        response = self.client.get(reverse('delete_booking', args=[booking.id]))
        # Check that user is being taken to 403 Forbidden page
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, '403.html')

    def test_my_bookings_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # # Check that user is being taken my bookings page
        response = self.client.get(reverse('my_bookings'))
        self.assertEqual(response.status_code, 200)
