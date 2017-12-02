from django import forms
from blog.models import Post
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size': 60}))
    slug = forms.CharField(widget=forms.TextInput(attrs={'size': 60}))
    intro = forms.CharField(widget=CKEditorWidget(attrs={'rows': 10}))
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        exclude = ()
        widgets = {
            'status': forms.RadioSelect,
        }

