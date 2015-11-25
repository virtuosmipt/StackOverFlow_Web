# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic import TemplateView
from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
import datetime




class registration(TemplateView):
    template_name = "registration.html"
class test(TemplateView):
    template_name = "test.html"
class registration(TemplateView):
    template_name = "registration_test.html"

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login_test.html',c)

def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        # Отображение страницы с ошибкой
        return HttpResponseRedirect('/accounts/invalid')  


def loggedin(request):
    return HttpResponseRedirect('/')
    
    #return render_to_response('/',{'full_name' : request.user.username,
                                               # 'user_name' : request.user.username})

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
def invalid_login(request):
    return render_to_response('invalid_login.html')
    
    
    
    


