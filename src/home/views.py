from django.shortcuts import render
from .forms import InputForm
from django.http import HttpResponseRedirect
from .PoSTagger import renderTreee
# Create your views here.

def home (request):
    return render(request, 'submit.html')

def renderTree(request):
    sentence = request.POST['name']
    sentence = renderTreee(sentence)
    sentence = "Your tree here!!"
    return render(request, 'result.html',{'result': sentence})
