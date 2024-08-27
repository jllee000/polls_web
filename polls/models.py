from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

#question 테이블 만듦
class Question(models.Model) :
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    question_num = models.IntegerField(default=0)

    def __str__(self) :
        return self.question_text
    def was_published_recently(self) :
        now = timezone.now()
        return now >= self.pub_date >= now-datetime.timedelta(days=1)

class Choice(models.Model) : 
    # question 테이블을 바라보는 외래키 생성, Question.id라고 굳이 안해도 pk 가져옴
    # on_delete 어저고 이건, Question id 관련 항목 삭제 시 관련된 행들 사라짐
    question = models.ForeignKey(Question , on_delete =models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self) :
        return self.choice_text