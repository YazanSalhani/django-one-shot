from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList
from todos.forms import TodoListForm

# Create your views here.
def todo_list_list(request):
    lists = TodoList.objects.all()
    context = {
    "lists": lists,
    }
    return render(request, "todos/list.html", context)

def todo_list_detail(request, id):
    list = get_object_or_404(TodoList, id=id)
    context = {
        "list": list
    }
    return render(request, "todos/detail.html", context)

def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            lists = form.save()
        return redirect("todo_list_detail", id=lists.id)
    else:
        form = TodoListForm()

    context = {
        "form" : form,
    }
    return render(request, "todos/create.html", context)
