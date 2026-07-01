from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def user_view(request):
    return HttpResponse("Here we hanlde multiple users (Authentication)")