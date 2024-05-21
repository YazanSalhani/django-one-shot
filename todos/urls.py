from django.urls import path
from todos.views import  todo_list_list

urlpatterns = [
    path('todos/', todo_list_list, name='home_page'),
]
