from multiprocessing import context
from pickle import TRUE
from typing_extensions import Self
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

from django.contrib.auth.views import LoginView

# Create your views here.
def index (request):
    tasks = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST' :

        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {'tasks':tasks,'form':form}  

    context['tasks']=context['tasks'].filter(user=request.user)

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
        return redirect('index')
    return render(request, 'new_item.html',{'todo':todo})








def update (request,pk):

    task = Todo.objects.get(id=pk)
    form = TodoForm(instance=task)

    if request.method == 'POST':
        form = TodoForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('index')


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

    return redirect('index')


from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login as auth_login

# Create your views here.

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('/')

    return render(request,'signup.html',{'form':form})