from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pun_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # Qusetion 외래키로 종속 Question이 지워질시 자동으로 Choice가 지워지도록 설정
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Charfield는 문자열로 이루어진 데이터필드를 의미 max_length로 글자수 제한을 할 수 있다.
    choice_text = models.CharField(max_length=200)
    # interFeild는 정수형 데이터필드이며 default값을 설정해줄 수 있다.
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
