from django.urls import path
from .views import *

urlpatterns = [
    path("", TodoListList.as_view(), name="viewlists"),
    path("createlist", TodoListCreate.as_view(), name="createlist"),
    path("updatelist/<pk>", TodoListUpdate.as_view(), name="updatelist"),
    path("deletelist/<pk>", TodoListDelete.as_view(), name="deletelist")
]