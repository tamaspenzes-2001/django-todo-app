from django import forms
from .models import *

class TodoListForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(TodoListForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['class'] = 'form-field'

  class Meta:
    model = TodoList
    fields = ("title",)