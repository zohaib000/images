from django.shortcuts import render
from home.models import img
# Create your views here.
def image(request):
    n=range(1,101)
    return render(request,"home/search.html",{"n":n})
