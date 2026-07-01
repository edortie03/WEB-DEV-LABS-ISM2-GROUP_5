from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def progress_index(request):
    return HttpResponse("This is where we track our Courses")