import imp
from pyexpat import model
from django.contrib import admin
from .models import CustomUser,UserType,Language


admin.site.register(CustomUser)
admin.site.register(UserType)
admin.site.register(Language)

