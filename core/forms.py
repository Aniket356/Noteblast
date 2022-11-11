from fileinput import FileInput
from django.forms import ModelForm, TextInput, FileInput, Textarea, NumberInput
from .models import Post

class NewPostForm(ModelForm):

  class Meta:
    model = Post
    fields = ('title', 'for_grade', 'description', 'attachment')

    widgets = {
      'title': TextInput(attrs={
        'class': ' mb-3 form-control'
      }),
      'for_grade': NumberInput(attrs={
        'class': 'mb-3 form-control'
      }),
      'description': Textarea(attrs={
        'class': 'mb-3 form-control',
      }),
      'attachment': FileInput(attrs={
        'class': 'mb-3 form-control'
      })
    }

class EditPostForm(ModelForm):

  class Meta:
    model = Post
    fields = ('title', 'description', 'attachment')
    
    widgets = {
      'title': TextInput(attrs={
        'class': ' mb-3 form-control'
      }),
      'description': Textarea(attrs={
        'class': 'mb-3 form-control',
        'style': 'white-space: pre-wrap'
      }),
      'attachment': FileInput(attrs={
        'class': 'mb-3 form-control'
      })
    }