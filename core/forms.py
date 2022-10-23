from fileinput import FileInput
from django.forms import ModelForm, TextInput, FileInput, Textarea
from .models import Post

class NewPostForm(ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'description', 'attachment')

    widgets = {
      'title': TextInput(attrs={
        'class': ' mb-3 form-control'
      }),
      'description': Textarea(attrs={
        'class': 'mb-3 form-control'
      }),
      'attachment': FileInput(attrs={
        'class': 'mb-3 form-control'
      })
    }
    