
from django.contrib import admin, auth
from questions.models import Question,Question_answer

admin.site.register(Question)
admin.site.register(Question_answer)

# Register your models here.
