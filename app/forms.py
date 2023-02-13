from django import forms
from.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'desc',
            'postPic',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'postPic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }