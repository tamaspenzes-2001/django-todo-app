from django.urls import path
from .views import *

urlpatterns = [
    path("", TodoListList.as_view(), name="viewlists"),
    path("createlist", TodoListCreate.as_view(), name="createlist")
]