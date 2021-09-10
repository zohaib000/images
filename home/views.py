from django.shortcuts import render
from home.models import img
# Create your views here.
def image(request):
    n=range(0,91)
    return render(request,"home/search.html")

def searching(request):
    n=range(0,875)
    return render(request,"home/searching.html",{"n":n})

def joker(request):
    n=range(0,492)
    return render(request,"home/joker.html",{"n":n})

def pig(request):
    n=range(0,492)
    return render(request,"home/pig.html",{"n":n})

def birds(request):    
    n=range(0,492)
    return render(request,"home/birds.html",{"n":n})

def lion(request):
    n=range(0,492)
    return render(request,"home/lion.html",{"n":n})
def tiger(request):
    n=range(0,492)
    return render(request,"home/tiger.html",{"n":n})
def fifa(request):
    n=range(0,492)
    return render(request,"home/fifa.html",{"n":n})
def poetry(request):
    n=range(0,492)
    return render(request,"home/poetry.html",{"n":n})
def animals(request):
    n=range(0,492)
    return render(request,"home/animals.html",{"n":n})

def parrot(request):
    n=range(0,492)
    return render(request,"home/parrot.html",{"n":n})

def cats(request):
    n=range(0,492)
    return render(request,"home/cats.html",{"n":n})

def dogs(request):
    n=range(0,492)
    return render(request,"home/dogs.html",{"n":n})
