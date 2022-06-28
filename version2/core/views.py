from multiprocessing import context
from pickle import TRUE
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index (request):
    tasks = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST' :

        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks,'form':form}        

    return render(request,'index.html',context)

def items(request,pk):
    todo = Todo.objects.get(id=pk)

    return render(request,'items.html',{'todo':todo})

def new_item(request,pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST['title']

        topic = TodoItem.objects.create(
            title = title,
            todo = todo
        )
        return redirect('/')
    return render(request, 'new_item.html',{'todo':todo})








def update (request,pk):

    task = Todo.objects.get(id=pk)
    form = TodoForm(instance=task)

    if request.method == 'POST':
        form = TodoForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'form':form}

    return render(request,'update.html',context)





def delete(request, pk):
    item = Todo.objects.get(id=pk)

    if request.method == 'POST':

        item.delete()

        return redirect('/')
    
    context = {'item':item}
    return render(request, 'delete.html', context)




def completeTodo(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()

    return redirect('/')