from .models import Comment, Post
from django import forms
from django.core.exceptions import ValidationError

override_error_messages = {
    'required': 'This field is required and cannot contain only whitespace.',
    'unique': 'Review with this title already exists.'
}


# This class is for the comments form to leave a comment
# and which fields I want to be shown

class CommentForm(forms.ModelForm):
    """
    This class is for the comment form.
    """
    body = forms.CharField(
        widget=forms.Textarea, error_messages=override_error_messages
    )

    class Meta:
        model = Comment
        fields = ('email', 'body',)

    # This function is to validate the body field and make
    # sure that maximum characters isn't exceeded

    def clean_body(self):
        body = self.cleaned_data.get('body')
        max_length = 1000
        if len(body) > max_length:
            raise forms.ValidationError(
                f'The maximum allowed characters for the '
                f'body is {max_length}.')
        return body

    # This function restricts the maximum characters in the field
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['maxlength'] = 1000


# This Class is for the Post / review form so that a user can leave a review

class ReviewForm(forms.ModelForm):
    """
    This class is for the leave a review form.
    """
    title = forms.CharField(error_messages=override_error_messages)
    content = forms.CharField(
        widget=forms.Textarea, error_messages=override_error_messages
    )

    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image',)

    # This function is to validate the title field and make
    # sure that maximum characters isn't exceeded

    def clean_title(self):
        title = self.cleaned_data.get('title')
        max_length = 50
        if len(title) > max_length:
            raise forms.ValidationError(
                f'The maximum allowed characters for the '
                f'title is {max_length}.')
        return title

    # This function is to validate the content field and make
    # sure that maximum characters isn't exceeded

    def clean_content(self):
        content = self.cleaned_data.get('content')
        max_length = 1000
        if len(content) > max_length:
            raise forms.ValidationError(
                f'The maximum allowed characters for the '
                f'content is {max_length}.')
        return content

    # This function is so that the image field doesnt appear as required as a
    # default image is provided if image is not selected.
    # Also restricts the maximum characcters allowed in the fields
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['maxlength'] = 50
        self.fields['content'].widget.attrs['maxlength'] = 1000
        self.fields['featured_image'].required = False
