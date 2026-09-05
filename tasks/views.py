from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskModelForm

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
