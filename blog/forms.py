from .models import Comment, Post
from django import forms
from django.core.exceptions import ValidationError

# This class is for the comments form to leave a comment
# and which fields I want to be shown

class CommentForm(forms.ModelForm):
    
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

    # This function is to validate the excerpt field and make sure just spaces
    # arent accepted
    def clean_excerpt(self):
        data = self.cleaned_data['excerpt']
        if data.strip() == '':
            raise ValidationError("Field should not contain only spaces.")
        return data
