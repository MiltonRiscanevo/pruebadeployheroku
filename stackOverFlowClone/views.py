from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializer import AnswerSerializer, QuestionSerializer
from .models import Question, Answers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt

def question_list(request):

    if request.method =='GET':
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(
            data = data
        )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status= 201)
        return JsonResponse(serializer.errors, status = 400)

def answer_list(request):
    if request.method == 'GET':
        answer = Answers.objects.all()
        serializer = AnswerSerializer(answer, many = True)
        return JsonResponse(serializer.data, safe= False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AnswerSerializer(
            data = data
        )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)