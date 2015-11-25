from django.core.management.base import BaseCommand, CommandError
from questions.models import Question, Question_answer
from likes.models import Question_answer_like, Question_like
from django.conf import settings
from userstore.models import  User
import string
import random

class Command(BaseCommand):


    def handle(self, *args, **options):
        i=1
        while i<50:
            q = Question_answer_like()
            q.question_answer_id = i
            q.user_id = 1
            q.save()
            i=i+1
