from django.db import models

# Create your models here.
class TodoList(models.Model):
  title = models.CharField(max_length=20)

  def get_absolute_url(self):
    return "/"

  def str(self):
    return self.title

class TodoItem(models.Model):
  text = models.CharField(max_length=30)
  checked = models.BooleanField(default=False)
  todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

  def str(self):
    return self.text