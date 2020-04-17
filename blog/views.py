from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')[:5]

class Postdetail(DetailView):
    model=Post





# def index(request):
#     posts = Post.objects.all().order_by('-created')[:5]
#
#     return render(request, 'blog/index.html', {
#         'posts':posts,
#     }
# )

# def post_detail(request,pk):
#     blog_post = Post.objects.get(pk=pk)
#     return render(request, 'blog/post_detail.html',{
#         'blog_post':blog_post,
#     })