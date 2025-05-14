from django.shortcuts import render, redirect, get_object_or_404

from .models import *

# Create your views here.

# print(Post.objects.all())

def mainpage(request):
  return render(request, 'main/mainpage.html')

def secondpage(request):
  posts = Post.objects.all()
  return render(request, 'main/secondpage.html', {'posts': posts})

def mainpage(request):
  context = {
    'generation': 13,
    'info': {'weather': '좋음', 'feeling': '배고픔(?)', 'note': '아기사자 화이팅!'},
    'shortKeys': [
      '들여쓰기: Tab',
      '내어쓰기: Shift + Tab',
      '주석 처리: 윈도우 - Ctrl + /, 맥 - command + /',
      '자동 정렬: Shift + Alt + F or Ctrl + K + F',
      '한 줄 이동: Alt + 방향키(위/아래)',
      '한 줄 삭제: Ctrl + Shift + k or Ctrl + x',
      '같은 단어 전체 선택: Ctrl + Shift + L'
    ]
  }
  return render(request, 'main/mainpage.html', context)

def new_post(request):
    return render(request, 'main/new-post.html')


def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'main/detail.html', {'post': post})


def edit(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {"post": edit_post})


def create(request):
  new_post = Post()
  new_post.title = request.POST['title']
  new_post.author = request.POST['author']
  new_post.body = request.POST['body']
  new_post.category = request.POST['category']
  new_post.image = request.FILES.get('image')
  
  new_post.save()
  return redirect('main:detail', new_post.id)

def update(request, id):
  update_post = Post.objects.get(pk=id)
  update_post.title = request.POST['title']
  update_post.author = request.POST['author']
  update_post.body = request.POST['body']
  update_post.category = request.POST['category']
  update_post.image = request.FILES.get('image')

  update_post.save()
  return redirect('main:detail', update_post.id)

def delete(request, id):
  delete_post = Post.objects.get(pk=id)
  delete_post.delete()
  return redirect('main:secondpage')