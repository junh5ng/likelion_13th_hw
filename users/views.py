from django.shortcuts import render, redirect, get_object_or_404
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
      'user':user
  }
  return render(request, 'users/mypage.html', context)

def follow(request, id):
  user = request.user
  followed_user = get_object_or_404(User, pk=id)
  is_follower = user.profile in followed_user.profile.followers.all()
  if is_follower:
    user.profile.followings.remove(followed_user.profile)
  else:
    user.profile.followings.add(followed_user.profile)
  return redirect('users:mypage', followed_user.id)