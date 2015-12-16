# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic import TemplateView
import datetime

from questions.forms import AskQuestion
from django.shortcuts import render, redirect
from django.contrib import auth
from questions.models import Question



class listquestion(TemplateView):
    template_name = "listquestion.html"
class question(TemplateView):
    template_name = "question.html"
class question_response(TemplateView):
    template_name = "question_response.html"

class MainView(TemplateView):
    template_name = "Main.html"

# Create your views here.


def ask(request):
    ask_form = AskQuestion(request.POST or None)
    args = {}
    args['form'] = ask_form
    if request.POST and ask_form.is_valid():
        question = Question(text_question=ask_form.cleaned_data['text'], title=ask_form.cleaned_data['title'])

        user = auth.get_user(request)
        question.user = user

        question.save()
        return render(request, 'question.html', args)
    else:
        return render(request, 'question.html', args)