from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from console import Console
import os

def face_recognition(request):
    dirname2 = os.path.join(os.getcwd(), 'pruebaInputs')
    imgpath2 = dirname2 + os.sep 
    images = []
    if request.method == 'POST':
        Image = request.FILES["image"]
        fs = FileSystemStorage()
        fs.save(Image.name, Image)
        Algorithm = request.POST["algorithm"]
        amount = request.POST["num"]
        console = Console()
        images = console.base(imgpath2, Algorithm, amount)

    return render(request, 'face_recognition.html', {"Artists": images})