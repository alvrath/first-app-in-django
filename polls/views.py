from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse

from .models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("Вы смотрите вопрос %s." % question_id)

def results(request, question_id):
    response = "Вы видите результаты вопроса %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Вы голосуете за вопрос %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
