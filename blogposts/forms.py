from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for adding a comment
    """
    class Meta:
        model = Comment
        fields = ('body',)


class CreatePostForm(forms.ModelForm):
    """
    Form for creating a new blog post.
    """
    class Meta:
        model = Post
        fields = ['featured_image', 'title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    """
    Form for editing an existing blog post.
    """
    class Meta:
        model = Post
        fields = ['featured_image', 'title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
