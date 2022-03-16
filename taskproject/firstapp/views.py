from django.http import HttpResponse
from django.shortcuts import render
from . models import star
from . models import players
# Create your views here.

def demo(request):
    obj = star.objects.all()
    objct = players.objects.all()

    return render(request,'index.html',{'result':obj,'res':objct})







# def operation(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add = x+y
#     mul = x*y
#     sub = x-y
#     div = x/y
#     return render(request,'result.html',{'add':add,'mul':mul,'sub':sub,'div':div})
#
# def page1(request):
#     return HttpResponse('You are re-directed to about')
#
# def page2(request):
#     return render(request,'page2.html')
#
# def details(request):
#     return HttpResponse("Welcome to page details")
#
# def thanks(request):
#     return render(request,'thanks.html')
