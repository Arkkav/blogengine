from django.shortcuts import render, get_object_or_404
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})  # by default searches in templates directory


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
    # def get(self, request, slug):  # process GET requests, no needs in "if else"...
    #     post = get_object_or_404(Post, slug__iexact=slug)  # class indeed + condition
    #     return render(request, 'blog/post_detail.html', context={'post': post})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'
    # def get(self, request, slug):
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     return render(request, 'blog/tag_detail.html', context={'tag': tag})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})
