from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy

from .forms import NewPostForm
from .models import UserBlogPost


# class view
class PostListView(generic.ListView):
    template_name = 'weblog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return UserBlogPost.objects.filter(user_status='pub').order_by('-user_datetime_modified')


# functional view
# def post_list_views(request):
#     all_post = UserBlogPost.objects.filter(user_status='pub').order_by('-user_datetime_modified')
#     return render(request, 'weblog/posts_list.html', {'posts_list': all_post})
# -------------------------------------------------------------------


class PostDetailViews(generic.DetailView):
    model = UserBlogPost
    template_name = 'weblog/post_detail.html'
    context_object_name = 'post'


# def post_detail_views(request, pk):
#     post = get_object_or_404(UserBlogPost, pk=pk)
#     # post = UserBlogPost.objects.get(pk=pk)
#     return render(request, 'weblog/post_detail.html', {'post': post})
# -------------------------------------------------------------------


class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'weblog/post_create.html'
    context_object_name = 'form'


# def add_new_post(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = NewPostForm()
#             return redirect('post_list')
#     else:
#         form = NewPostForm()
#
#     return render(request, 'weblog/post_create.html', context={'form': form})
# -------------------------------------------------------------------


class PostUpdateView(generic.UpdateView):
    model = UserBlogPost
    template_name = 'weblog/post_create.html'
    form_class = NewPostForm


# def post_update_view(request, pk):
#     post = get_object_or_404(UserBlogPost, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#
#     return render(request, 'weblog/post_create.html', context={'form': form})
# -------------------------------------------------------------------


class PostDeleteView(generic.DeleteView):
    model = UserBlogPost
    template_name = 'weblog/post_delete.html'

    # first option :
    success_url = reverse_lazy('post_list')

    # second option :
    # def get_success_url(self):
    #     return reverse('post_delete')


# def post_delete_view(request, pk):
#     post = get_object_or_404(UserBlogPost, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#
#     return render(request, 'weblog/post_delete.html', context={'post': post})
