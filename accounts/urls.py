from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
  path('signup/', views.signup_view, name='signup'),
  path('login/', views.Login.as_view(), name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('logged_out/', views.logged_out, name='logged_out'),
  path('profile/<username>/', views.profile_view, name='profile'),
  path('password_changed/', TemplateView.as_view(template_name='accounts/password_changed.html'), name='password_changed'),
  path('change_password/', views.password_change, name='change_password')
]