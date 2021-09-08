from django.shortcuts import render
from home.models import img
# Create your views here.
def image(request):
 
    return render(request,"home/search.html")
