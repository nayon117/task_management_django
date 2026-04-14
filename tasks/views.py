from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Task Management System!")

def contact(request):
    return HttpResponse("<h2 style='color:red'>This is the contact page</h2>")

def show_tasks(request):
    return HttpResponse("Here are all the tasks you have created.")

def show_specific_task(request, id):
    print("id", id)
    print("id type", type(id))
    return HttpResponse(f"Here is the specific task with ID {id} you requested.")
