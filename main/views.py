from django.shortcuts import render

# Create your views here.

def mainpage(request):
  return render(request, 'main/mainpage.html')

def secondpage(request):
  return render(request, 'main/secondpage.html')

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