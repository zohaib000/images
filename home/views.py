from django.shortcuts import render
from home.models import img
# Create your views here.
def image(request):
    n=range(0,91)
    return render(request,"home/search.html")

def searching(request):
    n=range(0,875)
    return render(request,"home/searching.html",{"n":n})
