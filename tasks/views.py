from datetime import date

from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskModelForm
from tasks.models import Task, TaskDetail, Project
from django.db.models import Count, Max, Min, Sum, Avg

# Create your views here.
def manager_dashboard(request):
    tasks = Task.objects.all()
    total_tasks = tasks.count()
    pending_tasks = Task.objects.filter(status='PENDING').count()
    in_progress_tasks = Task.objects.filter(status='IN_PROGRESS').count()
    completed_tasks = Task.objects.filter(status='COMPLETED').count()

    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'pending_tasks': pending_tasks,
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks
    }

    return render(request, 'dashboard/manager-dashboard.html', context)

def user_dashboard(request):
    return render(request, 'dashboard/user-dashboard.html')

def test(request):
    context = {
        "names" : ["hasibul", "hasan", "nayon"]
    }
    return render(request, 'test.html', context)

def create_task(request):
    form = TaskModelForm() #for GET

    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'task_form.html', {'form': form, 'message': 'Task created successfully!'})

    context = {"form": form}
    return render(request, 'task_form.html', context)


def view_task(request):
    #  task_count = Task.objects.aggregate(total_tasks = Count('id'))
    # ekta proect er under e kotogula task ache ta dekhate hobe.
    task_count = Project.objects.annotate(total_task = Count('task')).order_by('total_task')
     
    return render(request, 'show_task.html', {'task_count': task_count})
