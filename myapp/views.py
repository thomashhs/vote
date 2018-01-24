from django.shortcuts import render,render_to_response,get_object_or_404
from myapp.models import Question,Choice
from django.template.loader import get_template

# Create your views here.
def index(request):
    question_list=Question.objects.all()
    return render_to_response("index.html",{'question_list':question_list})

def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render_to_response("detail.html",{'question':question})

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
        selected_choice.c_votes+=1
        selected_choice.save()
        return render_to_response('result.html',{'question':question})
    except Exception as e:
        return render_to_response("detail.html",{'question':question,'error_message':e})