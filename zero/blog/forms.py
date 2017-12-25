from django import forms
from django.forms.widgets import Textarea
from blog.models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size': 60}))
    slug = forms.CharField(widget=forms.TextInput(attrs={'size': 60}))
    intro = forms.CharField(widget=Textarea(attrs={'rows': 6, 'cols': 125}))
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        exclude = ()
        widgets = {
            'status': forms.RadioSelect,
        }

