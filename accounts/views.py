from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .models import User
from django.contrib.auth.decorators import login_required

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



