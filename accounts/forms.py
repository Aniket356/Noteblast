from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import PasswordInput, TextInput, EmailInput, NumberInput

class PasswordChange(forms.Form):
  old_password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
    'type': 'password',
    'placeholder': 'Your old password',
    'class': 'form-control mb-3'
  }))

  new_password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
    'type': 'password',
    'placeholder': 'New Password',
    'class': 'form-control mb-3'
  }))

  confirm_new_password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
    'type': 'password',
    'placeholder': 'Confirm New Password',
    'class': 'form-control mb-3'
  }))

  def clean(self):
    if 'newpassword1' in self.cleaned_data and 'newpassword2' in self.cleaned_data:
      if self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
        raise forms.ValidationError("The two password fields did not match.")
    return self.cleaned_data