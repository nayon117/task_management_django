from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import TaskModelForm, TaskDetailModelForm
from tasks.models import Task, TaskDetail, Project
from django.db.models import Count, Max, Min, Sum, Avg, Q
from django.contrib import messages

# Create your views here.
def manager_dashboard(request):
    type = request.GET.get('type', 'all')

    

    counts = Task.objects.aggregate(
        total = Count('id'),
        pending_tasks = Count('id', filter=Q(status='PENDING')),
        in_progress_tasks = Count('id', filter=Q(status='IN_PROGRESS')),
        completed_tasks = Count('id', filter=Q(status='COMPLETED')),
    )

    # retrieve data
    base_query = Task.objects.select_related('details').prefetch_related('assigned_to')

    if type == 'pending':
        tasks = base_query.filter(status='PENDING')
    elif type == 'in_progress':
        tasks = base_query.filter(status='IN_PROGRESS')
    elif type == 'completed':
        tasks = base_query.filter(status='COMPLETED')
    else:
        tasks = base_query.all()

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
    task_form = TaskModelForm() #for GET
    task_detail_form = TaskDetailModelForm()

    if request.method == 'POST':
        task_form = TaskModelForm(request.POST) 
        task_detail_form = TaskDetailModelForm(request.POST)

        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, 'Task created successfully!')
            return redirect('create-task')

    context = {
        'task_form': task_form,
        'task_detail_form': task_detail_form
    }
    return render(request, 'task_form.html', context)


def view_task(request):
    #  task_count = Task.objects.aggregate(total_tasks = Count('id'))
    # ekta proect er under e kotogula task ache ta dekhate hobe.
    task_count = Project.objects.annotate(total_task = Count('task')).order_by('total_task')
     
    return render(request, 'show_task.html', {'task_count': task_count})
