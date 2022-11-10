from django import forms
from django.core.exceptions import ValidationError

class PasswordChange(forms.Form):
  old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
    'type': 'password',
    'placeholder': 'Your old password',
    'class': 'form-control mb-3'
  }))

  new_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
    'type': 'password',
    'placeholder': 'New Password',
    'class': 'form-control mb-3'
  }))

  confirm_new_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
    'type': 'password',
    'placeholder': 'Confirm New Password',
    'class': 'form-control mb-3'
  }))

  def clean(self):
    if 'new_password' in self.cleaned_data and 'confirm_new_password' in self.cleaned_data:
      if self.cleaned_data['new_password'] != self.cleaned_data['confirm_new_password']:
        self.add_error('confirm_new_password', ValidationError("The two password field didn't match"))

    return self.cleaned_data
