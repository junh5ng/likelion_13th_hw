from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from main.models import Post
from accounts.models import Profile

# Create your views here.
def mypage(request, id):
  user = get_object_or_404(User, pk=id)
  profile = Profile.objects.get(user=user)
  
  posts = Post.objects.filter(author=user)

  context = {
      'profile': profile,
      'posts': posts,
  }
  return render(request, 'users/mypage.html', context)