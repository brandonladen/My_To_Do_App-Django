from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import To_Do_List
from .forms import To_Do_List_Form
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def view_task(request):
    #task = To_Do_List.objects.all()
    task = To_Do_List.objects.filter(user=request.user)
    context = {
        'task' : task
    }
    return render(request, 'Todoapp/index.html', context)

@login_required
def create_task(request):
    if request.method == 'POST':
        form = To_Do_List_Form(request.POST)
        if form.is_valid():
            user_table = form.save()
            user_table.user = request.user
            user_table.save()
            return redirect('home')
    else:
        form = To_Do_List_Form()
    
    context = {
        'form': form
    }
    return render(request, 'Todoapp/add_task.html', context)
@login_required
def edit_task(request, taskid):
    task = get_object_or_404(To_Do_List, pk=taskid)
    if request.method == 'POST':
        form = To_Do_List_Form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = To_Do_List_Form(instance=task)
    
    context = {
        'form' : form,
        'task' : task
    }
    return render(request, 'Todoapp/edit_task.html', context)
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(To_Do_List, pk=task_id)
    task.delete()
    return redirect('home')