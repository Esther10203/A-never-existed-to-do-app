from dataclasses import field
from pyexpat import model
from django import forms
from .models import Post
from django.forms import ModelForm

class PostForm(forms.ModelForm):
   class Meta:
      model=Post
      fields= ['title', 'task', 'created_date']