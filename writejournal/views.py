from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

class updateEntryView(UpdateView):
        model = Post
        template_name = 'edit_entry.html'
        form_class = PostForm
        #fields = ['title', 'title_tag', 'body']

class deleteEntryView(DeleteView):
        model = Post
        template_name = 'delete_entry.html'
        success_url = reverse_lazy('index')