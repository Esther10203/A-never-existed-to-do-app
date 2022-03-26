import imp
from operator import mod
from pyexpat import model
from re import template
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

# crud (create read update and delete)
class PostCreateView(CreateView):
   model=Post
   template_name = 'post_create.html'
   fields = ['title', 'task', 'created_date']
   success_url = reverse_lazy('task_list')
class PostListView(ListView):
   model=Post
   template_name = 'post_list.html'
   context_object_name = 'post_list'

   def get_context_data(self, **kwargs):
      context = super(PostListView, self).get_context_data(**kwargs)
      return context
class PostDetailView(DetailView):
   model=Post
   template_name = 'post_detail.html'
   context_object_name = 'post'
class PostUpdateView(UpdateView):
   model=Post
   template_name = 'post_update.html'
   form_class = PostForm
   success_url = reverse_lazy('task_list')
class PostDeleteView(DeleteView):
   model=Post
   template_name='post_delete.html'
   success_url=reverse_lazy('task_list')