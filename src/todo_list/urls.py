from django.urls import path
from . import views

app_name = 'todo_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>', views.detail, name='detail'),
    path('new_todo', views.new_todo, name='new_todo'),
    path('delete_todo/<int:todo_id>', views.delete_todo, name='delete_todo'),
    path('edit_todo/<int:todo_id>', views.edit_todo, name='edit_todo'),
]