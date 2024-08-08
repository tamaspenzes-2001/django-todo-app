from django.urls import path
from .views import *

urlpatterns = [
    path("", TodoListList.as_view(), name="todolistlist"),
]