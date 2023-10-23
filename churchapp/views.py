from django.shortcuts import render,redirect 
from django.http import HttpResponse, HttpResponseNotFound
from churchapp.models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from churchapp.forms import *
from django.shortcuts import render, get_object_or_404
from .models import  *
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from .models import  *


# Create your views here.



def home(request):
    # Fetch recent events, sermons, and posts.
    recent_events = Eventchurch.objects.all().order_by('-date')
    recent_posts = Recentpost.objects.all().order_by('-id')

    context = {
        'recent_events': recent_events,
        'recent_posts': recent_posts,
    }
    return render(request, 'churchapp/home.html', context)



def index(request):
  
 
    context= {
        'section': {
        'title':'Welcome To First Christian Church',
    },
  }
        # Additional stories can be added to the list
    return render(request,"churchapp/index.html",context)

def sermons(request):
    # Fetch all sermons
    recent_sermons = Sermon.objects.all().order_by('-date')
    all_sermons = Sermon.objects.all()
     

     
    context = {
        'recent_sermons': recent_sermons,
        'all_sermons': all_sermons,
    }
    
    return render(request, 'churchapp/weekly.html', context)



def event_church(request):
    # Fetch all events
    recent_events = Eventchurch.objects.all().order_by('-date')
    all_events = Eventchurch.objects.all()

    context = {
        'all_events': all_events,
        'recent_events': recent_events,

    }
    return render(request, 'churchapp/home.html', context)

def recent_post(request):
    # Fetch all posts
    recent_posts = Recentpost.objects.all().order_by('-date')
    all_posts = Recentpost.objects.all()

    context = {
        'all_posts': all_posts,
        'recent_posts': recent_posts,

    }
    return render(request, 'churchapp/home.html', context)    
    
    

def signin(request):
    return render(request, "churchapp/signin.html",{'title':'signup'})

def authenticate(request):
    if request.method == 'POST' :
        username = request.POST.get('username', '')  
        username = request.POST['username']  
        password = request.POST['password']  

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')

        else:
            messages.info(request, 'Invalid Credentials') 
            return redirect('signin')

       
    else:
        return render(request, 'churchapp/signin.html',{'msg' 'Error Occured'}) 
    
def register(request):
    return render(request, 'churchapp/register.html',{'title':'register'})

def logout(request):
    auth.logout(request)  
    return redirect('signin')    

def process(request):
    if request.method == 'POST':
        f_name = request.POST['fname'] 
        l_name = request.POST['lname'] 
        user_name = request.POST['username']    
        email = request.POST['email'] 
        password = request.POST['password'] 
        c_password = request.POST.get('c_password')

        if password == c_password:
            if User.objects.filter(username = user_name).exists():
                print("username taken")
                messages.info(request, 'User name Taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Similar email exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name = f_name, email = email, last_name = l_name,
                password = password, username = user_name) 
                user.save()
                messages.info(request, 'Successfully saved to the database')
                return render(request, "churchapp\home.html",{'msg':"inserted successfully"})
    else:
        messages.info(request, 'Password confirmation failed')
        return redirect('register')  
    
def about(request):
    return render(request,"churchapp/about.html") 
  


def media(request):
    recent_uloads = Media.objects.all().order_by('-id') #This retrieves all the data from table
    all_uloads = Media.objects.all()
  
    context = {
        'all_uloads': all_uloads,
        'recent_uloads':recent_uloads,
    }
    return render(request, "churchapp/media.html", context)
