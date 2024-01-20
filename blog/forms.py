from .models import Comment, Post
from django import forms
from django.core.exceptions import ValidationError


# This class is for the comments form to leave a comment
# and which fields I want to be shown

class CommentForm(forms.ModelForm):
    """
    This class is for the comment form.
    """

    class Meta:
        model = Comment
        fields = ('email', 'body',)

    # This function is to validate the body field and make
    # sure that maximum characters isn't exceeded
    def clean_body(self):
        data = self.cleaned_data['body']
        max_length = self.fields['body'].max_length

        if len(data) > max_length:
            raise forms.ValidationError(
                f"Body cannot exceed {max_length} characters.")
        return data


# This Class is for the Post / review form so that a user can leave a review

class ReviewForm(forms.ModelForm):
    """
    This class is for the leave a review form.
    """

    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image',)

    # This function is to validate the title field and make
    # sure that maximum characters isn't exceeded
    def clean_title(self):
        data = self.cleaned_data['title']
        max_length = self.fields['title'].max_length

        if len(data) > max_length:
            raise forms.ValidationError(
                f"Title cannot exceed {max_length} characters.")
        return data

    # This function is to validate the content field and make
    # sure that maximum characters isn't exceeded

    def clean_content(self):
        data = self.cleaned_data['content']
        max_length = self.fields['content'].max_length

        if len(data) > max_length:
            raise forms.ValidationError(
                f"Content cannot exceed {max_length} characters.")
        return data

    # This function is so that the image field doesnt appear as required as a
    # default image is provided if image is not selected.
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['featured_image'].required = False
