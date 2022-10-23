from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView
from .models import Post
from accounts.models import User
from .forms import NewPostForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, ListView):
  model = Post
  template_name = 'core/home.html'
  context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
  model = Post
  context_object_name = 'post'
  template_name = 'core/post_detail.html'


def new_post(request):
  if request.POST:
    form = NewPostForm(request.POST, request.FILES)
    if form.is_valid():
      new_post = form.save(commit=False)
      new_post.posted_by = request.user
      new_post.save()
      return redirect(reverse('home'))
  else:
    form = NewPostForm()
  return render(request, 'core/new_post.html', {'form':form})