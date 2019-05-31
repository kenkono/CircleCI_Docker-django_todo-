from django.shortcuts import render
from .models import Todo
from django.shortcuts import get_object_or_404


def index(request):
    todos = Todo.objects.all().order_by('-updated_datetime')
    return render(request, 'todo_list/index.html', { 'todos': todos })


def detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, 'todo_list/detail.html', {'todo': todo})


def new_todo(request):
    return render(request, 'todo_list/new_todo.html')
