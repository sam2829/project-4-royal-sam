from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import GalleryImage


class TestGalleryModel(TestCase):
    """
    Test for Gallery Model
    """
    def test_gallery_model_upload(self):
        # Test that a Gallery image is being uploaded
        image = 'image1.jpg'
        caption = 'Caption 1'

        # Upoload Image
        GalleryImage.objects.create(image=image, caption=caption)

        # Check the image has been uploaded
        self.assertEqual(GalleryImage.objects.count(), 1)

        # Retrieve object from model
        gallery_image = GalleryImage.objects.get(caption=caption)

        # Check that the data matches what was uploaded
        self.assertEqual(gallery_image.caption, caption)
