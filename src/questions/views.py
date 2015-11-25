# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic import TemplateView
import datetime




class listquestion(TemplateView):
    template_name = "listquestion.html"
class question(TemplateView):
    template_name = "question.html"
class question_response(TemplateView):
    template_name = "question_response.html"

class MainView(TemplateView):
    template_name = "Main.html"

# Create your views here.
