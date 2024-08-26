from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout


# Create your views here.

def ragister_views(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return 'succes'
        
    return render(request, 'register.html')

def login_views(request):
    return render(request, 'login.html' )

