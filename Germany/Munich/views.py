
from cgitb import text
from django.shortcuts import render
from django.http import HttpResponse
from Munich.models import Subscribers,Prospects



# Create your views here.

def index(request):
    return render(request,'index.html')


def email(request):
    return render(request,'email.html')



def about(request):
        return render(request,'about.html')



def navigation(request):
    return render(request,'navigation.html')



def available(request):
    return render(request,'available.html')




def prospects(request):
    prospects=Prospects
    prospects.Email = ''
    prospects.First_name=''
    prospects.Last_name=''
    prospects.Comments=''

    
    
    return render(request,'prospects.html')



def newsubscriberinfo (request):
        email= Subscribers
        email.Email=''
        email.Name=''
        return render(request,'newsubscriberinfo.html')