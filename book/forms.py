from .models import Comment
from django import forms


# Post-a-comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('proposed_title', 'featured_image')
