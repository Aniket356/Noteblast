from ast import Pass
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm, PasswordChange
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.

def signup_view(request):
  if request.POST:
    form = CustomUserCreationForm(request.POST)

    if form.is_valid():
      user = form.save(commit=False)
      user.save()
      login(request, user)
      return redirect('/')

  else:
    form = CustomUserCreationForm()

  return render(request, 'registration/signup.html', {'form':form})

class Login(LoginView):
  template_name = 'registration/login.html'

def logout_view(request):
  logout(request)
  return redirect(reverse('logged_out'))

def logged_out(request):
  return render(request, 'registration/logged_out.html')

@login_required
def profile_view(request, username):
  return render(request, 'accounts/profile.html', {'profile_user': User.objects.get(username=username)})

@login_required
def password_change(request):
  if request.POST:
    form = PasswordChange(request.POST)
    if form.is_valid():
      newpassword=form.cleaned_data['new_password']
      username = request.user.username

      user = authenticate(username=username, password=form.cleaned_data['old_password'])

      if user is not None:
        user.set_password(newpassword)
        login(request, user)
        user.save()

        return redirect(reverse('password_changed'))
      else:
        return render(request, 'registration/change_password.html', {'error': 'You have entered wrong old password', 'form':form})

    else:
      return render(request, 'registration/change_password.html', {'error':'You have entered wrong old password','form': form})

  else:
    form = PasswordChange()

  return render(request, 'registration/change_password.html', {'form': form})
