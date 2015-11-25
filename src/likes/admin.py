
from django.contrib import admin, auth
from likes.models import Question_like,Question_answer_like

admin.site.register(Question_like)
admin.site.register(Question_answer_like)
