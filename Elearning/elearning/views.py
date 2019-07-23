from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request,'elearning/home.html')




def about(request):
    return render(request,'elearning/about.html')



def five(request):

     
     image = Exams.objects.all()


     return render(request,'elearning/five.html',{'image': image})


def six(request):
    return render(request,'elearning/six.html')

def seven(request):
    return render(request,'elearning/seven.html')


def eight(request):
    return render(request,'elearning/eight.html')
