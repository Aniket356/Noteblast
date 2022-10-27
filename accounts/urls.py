from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('signup/', views.signup_view, name='signup'),
  path('login/', views.Login.as_view(), name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('logged_out/', views.logged_out, name='logged_out'),
  path('profile/<username>/', views.profile_view, name='profile'),
]