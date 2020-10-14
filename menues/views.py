from django.shortcuts import render

# Create your views here.

from .models import Category,Menu
# Create your views here.


def menu(request):
    menues = Category.objects.all().order_by('priority')

    return render(request,'menues/menu.html',{'menuList': menues,}) 
