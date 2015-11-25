from django.core.management.base import BaseCommand, CommandError
from questions.models import Question, Question_answer
from django.conf import settings
from userstore.models import  User
from tags.models import Tags
import string
import random

class Command(BaseCommand):


    def handle(self, *args, **options):
        i=0
        while i<10:

            t = Tags()
            t.tags_name = randstring(5)
            t.save()
            i=i+1




def randstring(n):
        a = string.ascii_letters + string.digits

        return ''.join([random.choice(a) for i in range(n)])
