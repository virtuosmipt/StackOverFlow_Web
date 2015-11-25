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
        while i<1000:
            q = Question_like()
            q.question_id = i
            q.user_id = 1
            q.save()
            i=i+1




def randstring(n):
        a = string.ascii_letters + string.digits

        return ''.join([random.choice(a) for i in range(n)])