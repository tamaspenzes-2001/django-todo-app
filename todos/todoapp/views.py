from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

# Create your views here.
class TodoListList(ListView):
  model = TodoList
  template_name = "todoapp/index.html"

class TodoListCreate(CreateView):
  model = TodoList
  form_class = TodoListForm
  template_name = "todoapp/todo-list-create.html"

class TodoListUpdate(UpdateView):
  model = TodoList
  form_class = TodoListForm
  template_name = "todoapp/todo-list-update.html"