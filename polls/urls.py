from django.urls import path
from polls import views # 현재 폴더안에 있는 views파일
urlpatterns = [
    path('',views.index) #메인 url 뒤 도메인 뒤에의 추가 //
]
