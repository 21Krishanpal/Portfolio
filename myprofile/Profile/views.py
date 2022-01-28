from django.shortcuts import render,HttpResponse
from Profile.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        subject=request.POST.get('subject')
        message= request.POST.get('message')
        contact=Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, 'Thanku for Messaging me !!')

    return render(request,"index.html")