from .models import *
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

class StaffRequiredMixin(LoginRequiredMixin):
    def test_func(self):
        if self.requests.user:
            return self.requests.user.usertype == 'editor' or self.requests.user.usertype == 'admin'
    def handle_no_permission(self):
        return redirect(reverse_lazy('users:login'))
    