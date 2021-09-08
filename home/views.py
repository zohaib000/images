from django.shortcuts import render
from home.models import img
# Create your views here.
def image(request):
    images=img.objects.all()
    return render(request,"home/search.html",{"images":images})
