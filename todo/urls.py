from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.TodoHomePage,name='index'),
    path('add/',views.addNewTodo,name='add'),
    path('complete/<task_id>/',views.completeTodo,name='complete'),
    path('incomplete/<task_id>/',views.inCompleteTodo,name='incomplete'),
    path('delete/',views.deleteTodo,name='delete'),
    path('reset/',views.resetTodo,name='reset'),
]