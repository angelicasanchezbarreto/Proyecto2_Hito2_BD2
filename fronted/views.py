from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
#from console import Console

def face_recognition(request):
    if request.method == 'POST':
        Image = request.FILES["image"]
        fs = FileSystemStorage()
        fs.save(Image.name, Image)
        Algorithm = request.POST["algorithm"]
        neighbors = request.POST["num"]
    #answer = dic.print_in_console(tweets)
    names = ['Johnny Dep']
    return render(request, 'face_recognition.html', {"Artists": names})