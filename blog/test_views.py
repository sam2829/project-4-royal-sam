from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment
from .forms import CommentForm, ReviewForm


class TestPostViews(TestCase):
    """
    Test for Views
    """
    # Create a user and a posts / reviews
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.user,
            approved=True,
            slug='test-post'
        )

    def test_post_list_view(self):
        # Test if the PostList view renders successfully
        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews.html')

    def test_post_detail_view(self):
        # Test if the PostDetail view renders successfully for a specific post
        response = self.client.get(
            reverse('review_details', args=[self.post.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_details.html')

    def test_leave_review_view(self):
        # Test if the LeaveReview view renders successfully and
        # handles form submission
        self.client.login(username='testuser', password='testpassword')

        # Check if the view renders successfully
        response_get = self.client.get(reverse('leave_review'))
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(response_get, 'leave_review.html')

        # Check if the view handles form submission and redirects
        response_post = self.client.post(
            reverse('leave_review'),
            data={'title': 'New Review', 'content': 'New Content'}
        )
        self.assertEqual(response_post.status_code, 302)

    def test_post_like_view(self):
        # Test if the PostLike view responds with a
        # redirect when a user likes a post
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            reverse('review_like', args=[self.post.slug])
        )
        self.assertEqual(response.status_code, 302)
