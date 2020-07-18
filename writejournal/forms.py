from django import forms
from . models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'h-full-width'}),
            'title_tag': forms.TextInput(attrs={'class': 'h-full-width'}),
            'author': forms.Select(attrs={'class': 'h-full-width'}),
            'snippet': forms.TextInput(attrs={'class': 'h-full-width'}),
            'body': forms.Textarea(attrs={'class': 'h-full-width'}),
            
        }