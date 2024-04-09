from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from .models import *
# Register your models here.

class CustomAdmin(UserAdmin):
    model = User
    list_display = ('email', 'usertype', 'image','surname','created_at','is_active', )
    list_filter = ('usertype',)
    fieldsets = (
        (None, { 'fields': ('email', 'usertype','image','surname','password')}),
        ('Permissions',  {'fields': ( 'is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('email', 'usertype','image','surname','password', 'is_active','is_staff')}
        )
    )
    ordering=('email',)

admin.site.register(User, CustomAdmin)