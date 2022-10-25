from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView
from .models import Post
from .forms import NewPostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


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

  paginator = Paginator(posts, 10)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)  

  context = {'posts': posts, 'range': range(1, 13), 'page_obj': page_obj}

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

class DeletePost(DeleteView):
  model = Post
  template_name = 'core/delete_post.html'
  success_url = reverse_lazy('home')
