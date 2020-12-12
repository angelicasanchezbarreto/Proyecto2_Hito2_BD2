from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def face_recognition(request):
    #tweets = request.GET["tweet"]
    #dic = Console()
    #answer = dic.print_in_console(tweets)
    return render(request, 'face_recognition.html', {"Tweets": "hola"})