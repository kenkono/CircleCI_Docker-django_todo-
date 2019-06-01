from django.shortcuts import render, redirect
from .models import Todo
from django.shortcuts import get_object_or_404
from .forms import TodoForm
from django.views.decorators.http import require_POST


def index(request):
    todos = Todo.objects.all().order_by('-updated_datetime')
    return render(request, 'todo_list/index.html', { 'todos': todos })


def detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, 'todo_list/detail.html', {'todo': todo})


def new_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list:index')
    else:
        form = TodoForm
    return render(request, 'todo_list/new_todo.html', {'form': form})


@require_POST
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todo_list:index')


def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list:index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_list/edit_todo.html', {'form': form, 'todo': todo})

