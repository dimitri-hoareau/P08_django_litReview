from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'flux/post_list.html', {'posts': posts})