from datetime import date

from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskModelForm
from tasks.models import Task, TaskDetail, Project
from django.db.models import Count, Max, Min, Sum, Avg

# Create your views here.
def manager_dashboard(request):
    return render(request, 'dashboard/manager-dashboard.html')

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
