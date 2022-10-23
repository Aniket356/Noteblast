from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.forms import PasswordInput, TextInput, EmailInput, NumberInput

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['email', 'username', 'first_name', 'last_name', 'grade']

    widgets = {
      'email': EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Email"
      }),
      'username': TextInput(attrs={
        "class": "form-control",
        "placeholder": "Username"
      }),
      'first_name': TextInput(attrs={
        "class": "form-control",
        "placeholder": "First Name"
      }),
      'last_name': TextInput(attrs={
        "class": "form-control",
        "placeholder": "Last Name"
      }),
      'grade': NumberInput(attrs={
        "class": "form-control",
        "placeholder": "Class"
      }),
      'password1': PasswordInput(attrs={
        "class": "form-control"
      }),
      'password2': PasswordInput(attrs={
        "class": "form-control"
      }),
    }


class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'grade']
