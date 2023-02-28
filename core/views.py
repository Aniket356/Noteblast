from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView
from .models import Post
from .forms import NewPostForm, EditPostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied

@login_required
def home_view(request):
  def user_in_group(user, group):
    return user.groups.all().filter(name=group).exists()

  if not user_in_group(request.user, "Teachers"):
    posts = Post.objects.filter(posted_by__grade=request.user.grade) | Post.objects.filter(for_grade=request.user.grade)

  else:
    if request.GET.get('class') and request.GET.get('class') != 'Select a class':
      class_filter = request.GET.get('class')
      posts = Post.objects.filter(posted_by__grade=class_filter) | Post.objects.filter(for_grade=class_filter)
    else:
      posts = Post.objects.all()

  paginator = Paginator(posts, 10)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)  

  context = {'posts': posts, 'range': range(1, 13), 'page_obj': page_obj}

  return render(request, 'core/home.html', context)


class PostDetailView(LoginRequiredMixin, DetailView):
  model = Post
  context_object_name = 'post'
  template_name = 'core/post_detail.html'

@login_required
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


class DeletePost(LoginRequiredMixin, DeleteView):
  model = Post
  template_name = 'core/delete_post.html'
  success_url = reverse_lazy('home')

  def get_queryset(self):
    return super().get_queryset().filter(posted_by=self.request.user)

class EditPost(LoginRequiredMixin, UpdateView):
  model = Post
  form_class = EditPostForm
  template_name = 'core/edit_post.html'
  success_url = reverse_lazy('home')

  def get_queryset(self):
    return super().get_queryset().filter(posted_by=self.request.user)
