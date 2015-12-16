"""
1.listquestion
2.question- new question
3.question_response

"""


from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from django.contrib import admin
from questions.views import *
from questions.views import ask
# from questions.models import questionsBest




urlpatterns = [
    url(r'^listquestion/$', TemplateView.as_view(template_name="listquestion.html")),
    url(r'^question/$', ask),
    url(r'^question_response/$', TemplateView.as_view(template_name="question_response.html")),
    url(r'^$',TemplateView.as_view(template_name="Main.html"),name='home'),
    url(r'^last_questions/$',TemplateView.as_view(template_name="last_question.html"),name='last_questions'),
    # url(r'^last_questions/$', questionsBest ,name='last_questions'),
]
