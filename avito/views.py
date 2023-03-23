from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Post, File, PostCategory, Comment
from django.db.models import Q


@login_required
def index_list(request):
    posts = Post.objects.filter(status=1).order_by('-post_id')
    files = File.objects.select_related('post')
    categories = PostCategory.objects.all().order_by('name')
    return render(request, 'index.html', {'posts': posts, 'files': files, 'categories': categories})

@login_required
def post_detail(request, pk):
    posts = get_object_or_404(Post.objects.filter(
        status=1).order_by('-post_id'), pk=pk)
    files = File.objects.select_related('post')
    return render(request, 'post_detail.html', {'post': posts, 'files': files})

def search(request):
    query = request.GET.get("q")
    posts_search = Post.objects.filter(Q(status=1), Q(title__icontains=query)).order_by('-post_id')
    files = File.objects.select_related('post')
    categories = PostCategory.objects.all().order_by('name')
    return render(request, 'search_results.html', {'posts' : posts_search, 'files': files, 'categories': categories})

@login_required
def account(request):
    current_user = request.user
    reviews = Comment.objects.filter(user=current_user.id).order_by('-created')
    return render(request, 'account.html', {'reviews' : reviews})