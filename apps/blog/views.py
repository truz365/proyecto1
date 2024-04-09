from django.shortcuts import render
from .models import *

from django.views.generic import (
    TemplateView,
)

# Create your views here.

class ListPosts(TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super(ListPosts, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
