from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
# Create your views here.
def index(request) :
    # Question.objects.all()
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    # 위에 key 값임 ! text가 아님, 딕셔너리 식 key값으로 html에서 꺼내서 씀 
    return render(request, 'polls/index.html', context)

# 
def detail(request, question_id) : 
    # try문 대신 바로 검사 함수 있음 get_object_or_404
    # get_list_or_404는 튜플이나 리스트 형태
    # ++ 404 페이지도 커스텀 가능 : polls/templates/polls 내에 404.html 생성
    q = get_object_or_404(Question,id=question_id)
    # 어느테이블에서, 어떤 기준으로 꺼낼지 인자 넘김
    # try문
    # try :
    #     q= Question.objects.get(id=question_id)

    # #조건문
    # except Question.DoesNotExist :
    #     raise Http404('Question {} 데이터 없음'.format(question_id)) 
    #     # 특정 에러를 강제로 발생시키는 명령문
    return render(request, 'polls/detail.html',{'question':q})

def vote(request, question_id) :
    response = "you're voting on question {}"
    return HttpResponse(response.format(question_id))

def results(request, question_id) :
    return HttpResponse("you're looking at question {}".format(question_id))
