from .models import Comment, Post
from django import forms

# This class is for the comments form to leave a comment
# and which fields I want to be shown

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'body',)


# This Class is for the Post form so that a user can leave a review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image', 'excerpt',)