from datetime import date

from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskModelForm
from tasks.models import Task, TaskDetail, Project
from django.db.models import Count, Max, Min, Sum, Avg, Q

# Create your views here.
def manager_dashboard(request):
    tasks = Task.objects.select_related('details').prefetch_related('assigned_to').all()
    # total_tasks = tasks.count()
    # pending_tasks = Task.objects.filter(status='PENDING').count()
    # in_progress_tasks = Task.objects.filter(status='IN_PROGRESS').count()
    # completed_tasks = Task.objects.filter(status='COMPLETED').count()

    counts = Task.objects.aggregate(
        total = Count('id'),
        pending_tasks = Count('id', filter=Q(status='PENDING')),
        in_progress_tasks = Count('id', filter=Q(status='IN_PROGRESS')),
        completed_tasks = Count('id', filter=Q(status='COMPLETED')),
    )

    context = {
        'tasks': tasks,
        'counts': counts
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
