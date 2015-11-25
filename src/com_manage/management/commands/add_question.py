from django.core.management.base import BaseCommand, CommandError
from questions.models import Question, Question_answer
from tags.models import Tags
from django.conf import settings
from userstore.models import  User
import string
import random

class Command(BaseCommand):


    def handle(self, *args, **options):
        i=0
        t = Tags.objects.all()
        while i<10:
            q = Question()
            q.title = "New Question"
            q.user_id = 1
            q.text_question = randstring(100)
            q.save()

            for tag in t:
                q.tags.add(tag)


            i=i+1




def randstring(n):
        a = string.ascii_letters + string.digits

        return ''.join([random.choice(a) for i in range(n)])

