from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
# Create your views here.

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')[:5]






# def index(request):
#     posts = Post.objects.all().order_by('-created')[:5]
#
#     return render(request, 'blog/index.html', {
#         'posts':posts,
#     }
# )