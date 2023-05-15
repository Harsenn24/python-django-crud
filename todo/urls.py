
from django.urls import path
from .views import todo_create, list_detail, update_data, list_todo, delete_todo

urlpatterns = [
    # todo/test/
    # todo/test
    path('create', todo_create, name="Todo Create"),
    path('list', list_todo, name="Todo List"),
    path('list/<slug:id>', list_detail, name="Todo Detail"),
    path('update/<slug:id>', update_data, name="Todo Update"),
    path('delete/<slug:id>', delete_todo, name="Todo Delete"),
]
