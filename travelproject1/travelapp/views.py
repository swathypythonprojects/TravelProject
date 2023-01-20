from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from . models import Place
from . models import Team

# def demofun(request):
#     return HttpResponse("HELLO WORLD")

def demofun(request):
    obj = Place.objects.all()
    obj1=Team.objects.all()

    # value passing to html page..
    # name = "India"
    return render(request, 'index.html', {'result': obj,'result1':obj1})
# def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return HttpResponse("Contact Number Please...")
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,'result.html',{'result':res})
