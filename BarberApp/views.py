from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def index_2(request):
    return render(request,'index-2.html')

def index_3(request):
    return render(request,'index-3.html')

def index_4(request):
    return render(request,'index-4.html')