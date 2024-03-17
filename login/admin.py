# login/admin.py
from django.contrib import admin
from .models import CustomUser, Food

admin.site.register(CustomUser)
admin.site.register(Food)
