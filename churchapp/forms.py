from django import forms
from churchapp.models import *
from django.contrib.auth.forms import AuthenticationForm



class SermonForm(forms.ModelForm):
    class Meta:
        model = Sermon
        fields= "__all__"      



class EventchurchForm(forms.ModelForm):
    class Meta:
        model = Sermon
        fields= "__all__"   

class RecentPostForm(forms.ModelForm):
    class Meta:
        model = Recentpost
        fields= "__all__"        



class MediaForm(forms.ModelForm):
    class Meta:
        model =Media
        fields= "__all__"
