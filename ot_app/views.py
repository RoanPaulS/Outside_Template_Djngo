from django.shortcuts import render
from django.http import HttpResponse

def newHome(request):
    return render(request,'outTemp.html',{'name':'Paul'})
