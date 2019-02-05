from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import User_Info

# Register your models here.


admin.site.register(User_Info)
admin.site.unregister(Group)
admin.site.unregister(User)