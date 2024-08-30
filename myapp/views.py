from django.shortcuts import render,HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from .models import Cont


# Create your views here.
def index(request):
    return render(request,'index.html',{})

def contact(request):
    return render(request,'contact.html',{})

def about(request):
    return render(request,'about.html',{})    

def post(request):
    return render(request,'post.html',{})    

def table(request):
    data = Cont.objects.all()
    data1 = {'data' : data}
    return render(request,'table.html',data1)    

def signUpData(request):
    Name = request.POST.get('name','default')
    Email = request.POST.get('email','default')
    Password = request.POST.get('password','default')
    Contact = request.POST.get('contact','default')
    print(Name,Email,Password,Contact)   
   
    u = Cont(Name=Name,Email=Email,Password=Password,Contact=Contact)
    u.save()
    

    return HttpResponse("Thanks for submit...") 




