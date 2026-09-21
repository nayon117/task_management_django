from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from users.forms import CustomResigtrationForm

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = CustomResigtrationForm(request.POST)
        if form.is_valid():
            form.save()
            
        form = CustomResigtrationForm()
    return render(request, 'registration/register.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    return render(request, 'registration/login.html')
