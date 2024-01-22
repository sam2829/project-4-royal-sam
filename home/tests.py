from django.test import TestCase


class TestHomeViews(TestCase):
    """
    Test for home views.
    """

    def test_home_view(self):
        
        response = self.client.get('/')
        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'index.html')