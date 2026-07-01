from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def quiz_view(request):
    return HttpResponse("This is where tasks and quizzes will be hosted")