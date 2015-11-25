from django.db import models
from userstore.models import User
from tags.models import Tags
from django.conf import settings 

#from userstore.models import User

class QuestionQuerySet(models.QuerySet):
    def new_questions(self):
        return self.order_by('date')
    def query_question_tags(request,tagsName):
         q=Question.objects.filter(name_tags=tagsName)
         return q
    def questionsBest(request, kolvo=5):
        queryset = Question.objects.all().order_by('-rate')[:kolvo]
        return queryset
    def questionsBest(request, objects_num=5):
        queryset = Question.objects.all().order_by('-rate')[:objects_num]
        context = {
            "queryset": queryset,
        }
        return render(request, 'last_question.html', context)

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=10000, default='NEW QUESTION ')
    text_question = models.CharField(max_length=10000, default='SOME STRING')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    tags = models.ManyToManyField(Tags)
    rate = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    objects = QuestionQuerySet.as_manager()



class Question_answer(models.Model):
    text_answer = models.CharField(max_length=10000, default='SOME STRING')
    question = models.ForeignKey(Question)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
