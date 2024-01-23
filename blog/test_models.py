from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class TestPostModel(TestCase):
    """
    Test the blog Post model
    """

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )

    def test_post_creation(self):
        # Create a post / review
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test post.'
        )

        # Check that the post / review was created
        self.assertEqual(Post.objects.count(), 1)

        # Check the data in model is what was provided
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.slug, 'test-post')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.content, 'This is a test post.')

    def test_post_likes(self):
        # Test the number_of_likes
        # Creat Post /review
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test post.',
        )

        # Initially there is no likes
        self.assertEqual(post.number_of_likes(), 0)

        # Create a like
        self.user.blogpost_like.add(post)
        self.assertEqual(post.number_of_likes(), 1)

        # Create another user and another like
        another_user = User.objects.create_user(
            username='anotheruser', password='anotherpassword')
        another_user.blogpost_like.add(post)
        self.assertEqual(post.number_of_likes(), 2)

    def test_post_ordering(self):
        # Test the ordering of posts
        # Create post 1
        post1 = Post.objects.create(
            title='Post 1',
            slug='post-1',
            author=self.user,
            content='This is post 1.',
        )
        # Create post 2
        post2 = Post.objects.create(
            title='Post 2',
            slug='post-2',
            author=self.user,
            content='This is post 2.',
        )

        # Check that posts are ordered by created_on in descending order
        posts = Post.objects.all()
        self.assertEqual(posts[0], post2)
        self.assertEqual(posts[1], post1)


class TestCommentModel(TestCase):
    """
    Test the blog Comment model
    """

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )

    def test_comment_creation(self):
        # Create a post / review
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test post.',
        )
        # Create a comment
        comment = Comment.objects.create(
            post=post,
            name='Test Comment',
            email='test@example.com',
            body='This is a test comment.',
        )

        # Check that the comment is created
        self.assertEqual(Comment.objects.count(), 1)

        # Check the data in model is what was provided
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.name, 'Test Comment')
        self.assertEqual(comment.email, 'test@example.com')
        self.assertEqual(comment.body, 'This is a test comment.')

    def test_comment_ordering(self):
        # Test the ordering of comments
        # Create post / review
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test post.',
        )
        # Create comment 1
        comment1 = Comment.objects.create(
            post=post,
            name='Commenter 1',
            email='commenter1@example.com',
            body='This is comment 1.',
        )
        # Create comment 2
        comment2 = Comment.objects.create(
            post=post,
            name='Commenter 2',
            email='commenter2@example.com',
            body='This is comment 2.',
        )

        # Check that comments are ordered by created_on in ascending order
        comments = Comment.objects.all()
        self.assertEqual(comments[0], comment1)
        self.assertEqual(comments[1], comment2)
