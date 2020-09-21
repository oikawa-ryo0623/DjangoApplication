import datetime#python標準モジュール

from django.db import models
from django.utils import timezone#Djangoのタイムゾーン関連ユーティリティ

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date  published')

    #Question.objects.all()
    #一覧出そうとしたときに下の文がないと
    #<QuerySet [<Question: Question object (1)>]>
    #あると<QuerySet [<Question: What's up?>]>
    #おそらく中の文字(今回でいうとquestion_textを返す)
    def __str__(self):
        return self.question_text
    
    #一番最近のものを認識するため
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    


# Create your models here.
