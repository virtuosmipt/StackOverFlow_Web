from django.db import models
from questions.models import Question,Question_answer
from userstore.models import User
from django.conf import settings 


class Question_like(models.Model):

    question = models.ForeignKey(Question)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Question_answer_like(models.Model):
    question_answer = models.ForeignKey(Question_answer)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)