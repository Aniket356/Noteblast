from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView
from .models import Post
from accounts.models import User
from .forms import NewPostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


def home_view(request):
  def user_in_group(user, group):
    return user.groups.all().filter(name=group).exists()

  if not user_in_group(request.user, "Teachers"):
    posts = Post.objects.filter(posted_by__grade=request.user.grade) | Post.objects.filter(for_grade=request.user.grade)

  else:
    if request.GET.get('class'):
      class_filter = request.GET.get('class')
      posts = Post.objects.filter(posted_by__grade=class_filter) | Post.objects.filter(for_grade=class_filter)
    else:
      posts = Post.objects.all()

  context = {'posts': posts, 'range': range(1, 13)}

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