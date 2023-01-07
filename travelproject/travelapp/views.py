from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Person


# Create your views here.
def home(request):
    obj=Place.objects.all()
    ven=Person.objects.all()
    return  render(request,"index.html",{'result':obj,'output':ven,})

