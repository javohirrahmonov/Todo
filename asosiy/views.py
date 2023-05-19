from django.shortcuts import render,redirect
from .models import *
from .forms import *

def home(request):
    return render(request,'home.html')

def todo(request):
    if request.method == 'POST':
        f = TodoForm(request.POST)
        if f.is_valid():
            Todo.objects.create(
                nom = f.cleaned_data['nom'],
                time = f.cleaned_data.get('time'),
                batafsil = f.cleaned_data.get('batafsil'),
                status = f.cleaned_data.get('status')
        )
        return redirect('/todo/')
    content = {
        "todolar": Todo.objects.all(),
        "forma": TodoForm()
    }
    return render(request, 'todo_eski.html', content)

def todo_ochir(request,son):
    Todo.objects.filter(id=son).delete()
    return redirect("/todo/")



