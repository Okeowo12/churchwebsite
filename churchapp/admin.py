from django.contrib import admin
from churchapp.models import *

# Register your models here.
admin.site.register(Media)
admin.site.register(Eventchurch)
admin.site.register(Sermon)
admin.site.register(Recentpost)



#to rename site
admin.site.index_title = "First Christian church"
