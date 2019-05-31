from django.urls import path
from . import views

app_name = 'todo_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>', views.detail, name='detail'),
    path('new_todo', views.new_todo, name='new_todo'),
]