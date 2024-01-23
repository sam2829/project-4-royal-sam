from django.test import TestCase
from django.core.exceptions import ValidationError
from .forms import CommentForm, ReviewForm
from .models import Comment, Post
from django.contrib.auth.models import User


class TestCommentForm(TestCase):
    """
    Tests for Comment Form
    """
    def test_comment_form_valid(self):
        # Test the CommentForm is valid with correct data
        # Create user, post to comment on and form data.
        user = User.objects.create_user(username='testuser', password='testpassword')
        post = Post.objects.create(title='Test Post', content='Test Content', author=user)
        form_data = {'email': 'test@example.com', 'body': 'Test comment body'}
        form = CommentForm(data=form_data)
        # Check form is valid
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid_max_characters(self):
        # Test the CommentForm is invalid with incorrect data
        # by creating a field that exceeds the maximum characters
        form_data = {'email': 'test@example.com', 'body': 'A' * 1001}
        form = CommentForm(data=form_data)
        # Check form in invalid and body field raises error
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors)


class TestReviewForm(TestCase):
    """
    Test for Review Form
    """
    def test_review_form_valid(self):
        # Test the ReviewForm is valid with correct data
        # Create form data
        form_data = {'title': 'Test Title', 'content': 'Test Content'}
        form = ReviewForm(data=form_data)
        # Check form is valid
        self.assertTrue(form.is_valid())

    def test_review_form_invalid_max_characters(self):
        # Test the ReviewForm is invalid with incorrect data
        # by creating a field that exceeds the maximum characters
        form_data = {'title': 'A' * 51, 'content': 'A' * 1001}
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('content', form.errors)