from django.shortcuts import render
from .forms import InputForm
from django.http import HttpResponseRedirect
from .PoSTagger import renderTreee

import os
from syntaxTree.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL, BASE_DIR
# Create your views here.

def home (request):
    return render(request, 'submit.html')

def renderTree(request):
    sentence = request.POST['name']
    sentence = renderTreee(sentence)
    sentence = "Your tree here!!!"

    img_list = os.listdir(os.path.join(BASE_DIR) + "\\home\\static\\images") 
    print(img_list)

    context = {'result' : sentence, 'imgs': img_list}
    return render(request, 'result.html', context)
