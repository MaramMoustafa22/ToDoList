from multiprocessing import context
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

    return render(request,'core/index.html',context)



def update (request,pk):

    task = Todo.objects.get(id=pk)
    form = TodoForm(instance=task)

    if request.method == 'POST':
        form = TodoForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'form':form}

    return render(request,'core/update.html',context)





def delete(request, pk):
    item = Todo.objects.get(id=pk)

    if request.method == 'POST':

        item.delete()

        return redirect('/')
    
    context = {'item':item}
    return render(request, 'core/delete.html', context)



