from django.shortcuts import render
from .models import Data
from .models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def library(request):
    return render(request,'library.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')
        contact= Contact(name=name,email=email,phone=phone,subject=subject,message=message)
        contact.save()
      
        
    return render(request,'contact.html')

def books(request):
    return render(request,'books.html')


def detail(request):
    comment = Data.objects.all()
    context = {'comment':  comment}
    return render(request,'detail.html',context) 