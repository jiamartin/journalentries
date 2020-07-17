from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . models import Post


class indexView(ListView):
        model = Post
        template_name = 'index.html'

class entryView(DetailView):
        model = Post
        template_name = 'entry.html'

class addView(CreateView):
        model = Post
        template_name = 'add.html'
        fields = '__all__'

