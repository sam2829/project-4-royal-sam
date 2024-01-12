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

    # This function is to validate the body field and make sure just spaces
    # arent accepted
    def clean_body(self):
        data = self.cleaned_data['body']
        if data.strip() == '':
            raise ValidationError("Field should not contain only spaces.")
        return data

# This Class is for the Post / review form so that a user can leave a review

class ReviewForm(forms.ModelForm):
    """
    This class is for the leave a review form.
    """

    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image', 'excerpt',)

    # This function is to validate the title field and make sure just spaces
    # arent accepted
    def clean_title(self):
        data = self.cleaned_data['title']
        if data.strip() == '':
            raise ValidationError("Field should not contain only spaces.")
        return data

    # This function is to validate the content field and make sure just spaces
    # arent accepted
    def clean_content(self):
        data = self.cleaned_data['content']
        if data.strip() == '':
            raise ValidationError("Field should not contain only spaces.")
        return data

    # This function is so that the image field doesnt appear as required as a   
    # default image is provided if image is not selected.
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['featured_image'].required = False
