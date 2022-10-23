from django.urls import path
from . import views

urlpatterns = [
  path('', views.home_view, name='home'),
  path('new/', views.new_post, name='create_post'),
  path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]