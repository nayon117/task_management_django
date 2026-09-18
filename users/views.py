from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.forms import CustomResigtrationForm, RegisterForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomResigtrationForm(request.POST)
        if form.is_valid():
            form.save()
            
    if request.method == 'GET':
        form = CustomResigtrationForm()
    return render(request, 'registration/register.html', {'form': form})
