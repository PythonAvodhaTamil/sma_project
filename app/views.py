from django.shortcuts import redirect, render
from app.models import User
from django.contrib import messages
from django.contrib import auth 
# Create your views here.
def home (request):
    return render (request,"index.html")

def sign_up (request):
    
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"E-mail is already taken")
                return redirect ('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"username is already taken")
                return redirect ('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()

        else:
            messages.info(request,"password is not matching")
            return redirect ('signup')
      
    else:   
        return render (request,"signup.html")

def signin (request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        
        else:
            messages.info(redirect,"user and password doesn't exist")
            return redirect ('signin')
            

    else:
        return render (request,"signin.html")    
    
    
    
    
    
    
    
    