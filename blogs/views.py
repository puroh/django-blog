from django.shortcuts import render

from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
    Return all posts that are with status 1 (published) and order from the latest one.
    """

    queryset = Post.objects.filter(status=1).order_by("-created_at")
    template_name = "snippets/list.html"
    # context_object_name = "my_book_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Post"
        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog.html"


class IndexView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_at")
    template_name = "index.html"
