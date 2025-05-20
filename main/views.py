from django.shortcuts import render, redirect, get_object_or_404

from .models import *
import re

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
  if request.method == 'GET':
    comments = Comment.objects.filter(post=post)
    return render(request, 'main/detail.html', {'post':post, 'comments': comments})
  
  elif request.method == 'POST':
    new_comment = Comment()
    new_comment.post = post
    new_comment.author=request.user
    new_comment.body = request.POST['content']
    new_comment.save()
    return redirect('main:detail', id)

def delete_comment(request, comment_id):
  comment = get_object_or_404(Comment, pk=comment_id)

  if request.user == comment.author:
    comment.delete()

  return redirect('main:detail', comment.post.id)

def edit(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {"post": edit_post})


def create(request):
  if request.user.is_authenticated:
    new_post = Post()
    new_post.title = request.POST['title']
    # new_post.author = request.POST['author']
    new_post.author = request.user
    new_post.body = request.POST['body']
    new_post.category = request.POST['category']
    new_post.image = request.FILES.get('image')
    
    new_post.save()

    #본문을 띄어쓰기 + 엔터 기준으로 나누기
    words = re.split(r'\s+', new_post.body)

    tag_list = []
    # 나눈 단어가 '#'으로 시작한다면 tag_list에 저장
    for w in words:
      if len(w)>0:
        if w[0] == '#':
          tag_list.append(w[1:])
          for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_post.tags.add(tag.id)

    return redirect('main:detail', new_post.id)
  else:
    return redirect('accounts:login')

def update(request, id):
  update_post = Post.objects.get(pk=id)
  if request.user.is_authenticated and request.user == update_post.author:
    update_post.title = request.POST['title']
    # update_post.author = request.POST['author']
    update_post.body = request.POST['body']
    update_post.category = request.POST['category']
    
    if request.FILES.get('image'):
      update_post.image = request.FILES.get('image')
    update_post.save()

    #본문을 띄어쓰기 + 엔터 기준으로 나누기
    update_post.tags.clear()

    words = re.split(r'\s+', update_post.body)

    tag_list = []
    # 나눈 단어가 '#'으로 시작한다면 tag_list에 저장
    for w in words:
      if len(w)>0:
        if w[0] == '#':
          tag_list.append(w[1:])
          for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            update_post.tags.add(tag.id)

    return redirect('main:detail', update_post.id)
  return redirect('accounts:login', update_post.id)

def delete(request, id):
  delete_post = Post.objects.get(pk=id)
  delete_post.delete()
  return redirect('main:secondpage')

def tag_list(request): #모든 태그 목록을 볼 수 있는 페이지
    tags = Tag.objects.all()
    return render(request, 'main/tag-list.html', {'tags': tags})

def tag_posts(request, tag_id): #특정 태그를 가진 게시글의 목록을 볼 수 있는 페이지
    tag=get_object_or_404(Tag, id=tag_id)
    posts=tag.posts.all()
    return render(request, 'main/tag-post.html', {
        'tag' : tag,
        'posts' : posts
    })