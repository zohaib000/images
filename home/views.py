from django.shortcuts import render
from home.models import img
# Create your views here.
def image(request):
    images=img.objects.all()
    for i in images:
        print(i.name)
    return render(request,"home/search.html")