from django.urls import path
from polls import views # 현재 폴더안에 있는 views파일
urlpatterns = [
    path('',views.index, name='index'), #메인 url 뒤 도메인 뒤에의 추가 //
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:qustion_id>/vote/', views.vote, name='vote'),
    path('<int:qustion_id>/results/', views.results, name='result')
]

