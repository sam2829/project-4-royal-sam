from django.test import TestCase
from django.urls import reverse
from .models import GalleryImage


class TestGalleryViews(TestCase):
    """
    Test for Gallery views.
    """
    @classmethod
    def setUpTestData(cls):
        # Create some test GalleryImage objects as the model
        GalleryImage.objects.create(image='image1.jpg', caption='Caption 1')
        GalleryImage.objects.create(image='image2.jpg', caption='Caption 2')

    def test_gallery_view(self):

        response = self.client.get(reverse('gallery'))
        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'gallery.html')
        # Check the images are present
        self.assertIn('images', response.context)
        # Check the images are loading on the page
        self.assertContains(response, 'image1.jpg')
        self.assertContains(response, 'image2.jpg')
        # Check that the number of images in the context is correct
        self.assertEqual(len(response.context['images']), 2)
