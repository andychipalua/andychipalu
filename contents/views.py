from django.shortcuts import render
from django.http import HttpResponse

from .models import HTMLBlock
# Create your views here.


def privacy(request):
    contentName = "privacy"
    return blockPage(request,contentName)    


def policy(request):
    contentName = "policy"
    return blockPage(request,contentName)   
   
    

def blockPage(request,contentName):
    try:
        content = HTMLBlock.objects.get(name=contentName)
    except HTMLBlock.DoesNotExist:
        raise http404('Content not found')
    return render(request,'contents/page.html',{'content': content,})