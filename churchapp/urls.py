from django.urls import path,include
from churchapp.views import *
from . import views


urlpatterns = [
path("signin/",signin,name="signin"), 
path('logout', logout, name= 'logout'), 
path("",index,name="home"),    
path("home/",views.home,name="home"),
path("about/",about,name="about"),  
path("media/",views.media,name="media"),
path("authenticate", views.authenticate, name='authenticate'),
path("process/",views.process,name="process"),
path("sermons/",views.sermons,name="sermons"),
path("register/",register,name="register"),

]