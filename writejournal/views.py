from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . models import Post
from . forms import PostForm
from django.urls import reverse_lazy


class indexView(ListView):
        model = Post
        template_name = 'index.html'
        ordering = ['-id']

class entryView(DetailView):
        model = Post
        template_name = 'entry.html'

class addView(CreateView):
        model = Post
        form_class = PostForm
        template_name = 'add.html'

