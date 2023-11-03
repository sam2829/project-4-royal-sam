from .models import Comment
from django import forms

# This class is for the comments form to leave a comment
# and which fields i want to be shown

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'body',)