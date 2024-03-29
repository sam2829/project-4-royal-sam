from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# This class is for the necessary fields to post model


class Post(models.Model):
    """
    This model is for all the fields needed for the user or admin to leave
    a review / post.
    """

    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=1000)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    approved = models.BooleanField(default=False)

    # The minus before the created_on field means the posts will be in
    # descending order

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

# This class is for the necessary fields for the comments model


class Comment(models.Model):
    """
    This class is for all the fields needed to comment on reviews / posts.
    """

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # This created_on field will allow the comments to be in ascending order

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
