from django.shortcuts import render
from django.http import HttpResponse

# views here.

def course_index(request):
    return HttpResponse("This is a Course app. Welcome to the courses platfrom")

