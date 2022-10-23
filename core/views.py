from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView
from .models import Post
from accounts.models import User
from .forms import NewPostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group


def home_view(request):
  def user_in_group(user, group):
    return user.groups.all().filter(name=group).exists()

  if user_in_group(request.user, "Students"):
    posts = Post.objects.filter()

  else:
    posts = Post.objects.all()

  context = {'posts': posts}

  return render(request, 'core/home.html', context)


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