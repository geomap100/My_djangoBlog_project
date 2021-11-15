from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    #return HttpResponse('Hello_World!')
     return render(request,'about.html')
def home(request):
    #return HttpResponse
     return render(request,'home.html')