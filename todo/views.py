from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST


def TodoHomePage(request):
	listOfTasks=Todo.objects.order_by('id')
	form=TodoForm()
	context={
	'todo_list':listOfTasks,
	'form':form
	}
	return render(request,'index.html',context)

@require_POST
def addNewTodo(request):
	form=TodoForm(request.POST)
	if form.is_valid:
		new_task=Todo(task=request.POST['task'])
		new_task.save()
	return redirect('index')

def completeTodo(request,task_id):
	completed_task=Todo.objects.get(pk=task_id)
	completed_task.isComplete=True
	completed_task.save()
	return redirect('index')


def deleteTodo(request):
	Todo.objects.filter(isComplete__exact=True).delete()
	return redirect('index')

def inCompleteTodo(request,task_id):
	completed_task=Todo.objects.get(pk=task_id)
	completed_task.isComplete=False
	completed_task.save()
	return redirect('index')		

def resetTodo(request):
	Todo.objects.all().delete()
	return redirect('index')
