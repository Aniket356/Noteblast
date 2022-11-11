from django.urls import path
from . import views

urlpatterns = [
  path('', views.home_view, name='home'),
  path('new/', views.new_post, name='create_post'),
  path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
  path('<slug>/delete/', views.delete_post, name='delete_post'),
  path('<slug>/edit/', views.EditPost.as_view(), name='edit_post')
]