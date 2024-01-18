from django.test import TestCase


class TestHomeViews(TestCase):
    """
    Test for home views.
    """

    def test_home_view(self):

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')