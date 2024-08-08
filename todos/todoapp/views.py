from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.
class TodoListList(ListView):
  model = TodoList
  template_name = "todoapp/index.html"
