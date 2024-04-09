from django.db import models 
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):
    
    def _create_user(self, email, password, is_staff, is_superuser, is_active, **extra_fields) :
        
        user = self.model(
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active = True,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, is_active=True, **extra_fields):
        return self._create_user(email, password, False, False, True, **extra_fields)
    
    def create_superuser(self, email, password=None, is_staff=True, is_superuser=True, is_active=True, **extra_fields):
        return self._create_user(email, password, True, True, True, **extra_fields)