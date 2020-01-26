from django.shortcuts import render,redirect
from .models import Todo #naimportujeme nasu class Todo a vytiahneme si znej Objekty
from .forms import TodoForm
from django.contrib.auth.decorators import login_required


def todoview(request):
        todo_list = Todo.objects.filter(author=request.user) #priradujeme objekty do listu
        form = TodoForm(request.POST) #vyberie prvok z inputu
        if form.is_valid(): #skontroluje ci je tam text
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save() #ulozi k ostatnym objektom
            return redirect("todo")
        context = {
            "todo_list":todo_list,
            "form":form
            }
        return render(request , "todo_list.html", context)

def home(request):
    return render(request,'home.html',)

def Done(request,pk):
    query = Todo.objects.get(pk = pk)
    query.done = True
    query.save()
    return redirect("todo")

def NotDone(request,pk):
    query = Todo.objects.get(pk=pk)
    query.done = False
    query.save()
    return redirect("todo")

def Delete(request,pk):
    query = Todo.objects.get(pk = pk)
    query.delete()
    return redirect("todo")
