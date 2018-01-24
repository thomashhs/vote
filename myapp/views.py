from django.shortcuts import render,render_to_response
from myapp.models import Question,Choice
from django.template.loader import get_template

# Create your views here.
def index(request):
    question_list=Question.objects.all()
    return render_to_response("index.html",{'question_list':question_list})
