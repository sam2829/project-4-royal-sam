from django.test import TestCase
from django.urls import reverse


class TestContactUsViews(TestCase):
    """
    Test for Contact Us views.
    """

    def test_contact_us_view(self):

        response = self.client.get(reverse('contact_us'))
        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'contact_us.html')
        # Check if the Google API key is present
        self.assertIn('GOOGLE_API_KEY', response.context)
