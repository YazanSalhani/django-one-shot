from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoList
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

def todo_list_update(request, id):
    todo_list = get_object_or_404(TodoList,id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance = todo_list)
        if form.is_valid():
            todo_list = form.save()
        return redirect("todo_list_detail", id=todo_list.id)
    else:
        form = TodoListForm(instance = todo_list)

    context = {
        "form" : form,
        "todo_list" : todo_list,
    }
    return render(request, "todos/update.html", context)

def todo_list_delete(request, id):
  list = TodoList.objects.get(id=id)
  if request.method == "POST":
    list.delete()
    return redirect("todo_list_list")
  return render(request, "todos/delete.html")
