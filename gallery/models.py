from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# This class is for the necessary fields for gallery photos


class GalleryImage(models.Model):
    """
    This model is to store images for the gallery.
    """

    image = CloudinaryField('image')
    caption = models.CharField(max_length=100)
